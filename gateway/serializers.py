from rest_framework import serializers
from user.models import User
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from gateway.utils import Util
from rest_framework.exceptions import AuthenticationFailed

class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField()
    phone_number = serializers.CharField()
    password = serializers.CharField()


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class RefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField()

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.CharField(min_length=2)

    def validate(self, attrs):
        
        email = attrs["data"].get('email', '')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uibd64 = urlsafe_base64_encode(user.id)
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(request=attrs["data"].get("request")).domain
            relative_link = reverse("password-reset", kwargs={"uidb64":uibd64, "token":token})
            # absurl = "http://"+current_site+relative_link+"?token="+token
            absurl = f"http://{current_site}{relative_link}"
            email_body = f" Hi {user.name}\n\nPlease use the link below to reset your password\n\n{absurl}\n\n"
                        
            data = {"email_body": email_body, "email_subject":"Reset your password", "to_email":user.email }
            Util.send_email(data)
            
        return super().validate(attrs)

class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=6, max_length=50, write_only=True)
    token = serializers.CharField(min_length=1, write_only=True)
    uidb64 = serializers.CharField(min_length=1, write_only=True)

    def validate(self, attrs):
        try:
            password=attrs.get("password")
            token=attrs.get("token")
            uidb64 = attrs.get("uidb64")

            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed("The reset link is invalid", 401)
            user.set_password(password)
            user.save()
            return user
        except Exception as e:
            raise AuthenticationFailed("The reset link is invalid", 401)
        return super().validate(attrs)

        