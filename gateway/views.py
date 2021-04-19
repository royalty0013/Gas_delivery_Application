import jwt
from gateway.models import Jwt
from user.models import User
from datetime import datetime, timedelta
from django.conf import settings as st
import random
import string
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from gateway.serializers import LoginSerializer, PasswordResetSerializer, RegistrationSerializer, RefreshSerializer, ChangePasswordSerializer,SetNewPasswordSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from django.db import IntegrityError
from gateway.utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from gateway.authentications import Authentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError, force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
# Create your views here.

def get_random(length):
    ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def get_access_token(payload):
    return jwt.encode(
        {"exp":datetime.now() + timedelta(minutes=5), **payload},
        st.SECRET_KEY,
        algorithm="HS256"
    )

def get_refresh_token():
    return jwt.encode(
        {"exp": datetime.now() + timedelta(days=365), "data":get_random(10)},
        st.SECRET_KEY,
        algorithm="HS256"
    )

class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username = serializer.validated_data['email'],
            password = serializer.validated_data['password']
        )

        if not user:
            return Response({"error":"Invalid Username or Password"}, status=status.HTTP_400_BAD_REQUEST)
        Jwt.objects.filter(user_id=user.id).delete()

        access = get_access_token({"user_id":user.id})
        refresh = get_refresh_token()

        Jwt.objects.create(
            user_id=user.id, access=access.decode(), refresh=refresh.decode()
        )
        email= serializer.validated_data['email']
        user_details = User.objects.get(email=email)

        response ={
            "name":user_details.name,
            "email":user_details.email,
            "phone_number":user_details.phone_number,
            "user_type":user_details.user_type,
            "verification status":user_details.is_verified,
            "active status":user_details.is_active,
            "account creation date":user_details.created_at,
            "status_code": 200,
            "token": access,
            "message": "User logged in successfully"
        }
        return Response(response)

# class RefreshTokenView(APIView):
#     serializer_class = RefreshSerializer
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         try:
#             active_jwt = Jwt.objects.get(refresh=serializer.validated_data["refresh"])
#         except Jwt.DoesNotExist:
#             return Response({"Error":"Token not found"}, status=status.HTTP_400_BAD_REQUEST)

#         if not Authentication.verify_token(serializer.validated_data["refresh"]):
#             return Response({"error":"Token has expired or invalid"})

#         access = get_access_token({"user_id":active_jwt.user_id})
#         refresh = get_refresh_token()

#         active_jwt.access = access.decode()
#         active_jwt.refresh = refresh.decode()
#         active_jwt.save()
 
#         return Response({"access":access, "refresh":refresh})

class RegisterView(APIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            User.objects._create_user(**serializer.validated_data)
            user_data = serializer.data
            user = User.objects.get(email=user_data["email"])

            access_token = get_access_token({"user_id":user.id})
            access_token = access_token.decode()

            current_site = get_current_site(request).domain
            relative_link = reverse("verify-email")
            # absurl = "http://"+current_site+relative_link+"?token="+token
            absurl = f"http://{current_site}{relative_link}?token={access_token}"
            email_body = f" Hi {user.name}\n\nPlease use the link below to verify your email address\n\n{absurl}\n\n"
            email_body += "please note the verification link expires in 5 minutes"
            
            data = {"email_body": email_body, "email_subject":"Please verify your email", "to_email":user.email }
            Util.send_email(data)

            response = {
                "name" : user.name.title(),
                "email":user.email.lower(),
                "phone_number":user.phone_number,
                "message": "Verification email sent to your mail"
            }
            return Response(response, status=status.HTTP_201_CREATED)

        except IntegrityError:
            return Response({"Error": "Email already exist"})
        # return Response({"success": "User Created"})
        
class verifyEmailView(APIView):
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, st.SECRET_KEY)
            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            
            return Response({"email":"Email is successfully activated"}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError:
            return Response({"error": "Activation Expired"}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError:
            return Response({"error": "Invalid Token"}, status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer

    model = User
    permission_classes = [IsAuthenticated]

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"Error":"The password is incorrect"}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()

            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'password updated successfully',
                'data': []
            }
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class passwordResetView(generics.GenericAPIView):
    serializer_class = PasswordResetSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        email = request.data["email"]

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            # uibd64 = urlsafe_base64_encode(user.id)
            uidb64 = urlsafe_base64_encode(force_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(request).domain
            relative_link = reverse("password-reset", kwargs={"uidb64":uidb64, "token":token})
            absurl = f"http://{current_site}{relative_link}"
            email_body = f" Hi {user.name}\n\nPlease use the link below to reset your password\n\n{absurl}\n\n"
                        
            data = {"email_body": email_body, "email_subject":"Reset your password", "to_email":user.email }
            Util.send_email(data)
        
        return Response({"success": "A link has been sent to reset your password"}, status=status.HTTP_200_OK)

class PasswordTokenCheckView(generics.GenericAPIView):

    def get(self, request, uidb64, token):
        try:
            id=smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({"error": "Token is not valid, please request a new one"}, status=status.HTTP_401_UNAUTHORIZED)

            return Response({"success": True, "Message": "Credential is valid", "uidb64": uidb64, "token": token}, status=status.HTTP_200_OK)
        
        except DjangoUnicodeDecodeError as identifier:

            return Response({"error": "error"})

class setNewPasswordView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"success":True, "Message":"Password reset successful"}, status=status.HTTP_200_OK)



