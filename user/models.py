from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import math
# Create your models here.

USERS = (
    ("Customer", "Customer"),
    ("Vendor", "Vendor"),
    ("Transporter", "Transporter"),
)

class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Incorrect Email Address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('name', 'admin')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self._create_user(email, password, **extra_fields)
        

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    user_type = models.CharField(max_length=20, choices=USERS, default="Customer")
    device_token = models.CharField(max_length=100, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    USERNAME_FIELD = "email"
    objects = UserManager()

    def __str__(self):
        return self.email

class Vendor_shop(models.Model):
    vendor = models.OneToOneField(User, related_name="vendor_shop", on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField()
    phone_number = models.CharField(max_length=30, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name_plural = "Vendors"
        
class Transporter(models.Model):
    transporter = models.OneToOneField(User, related_name="transporter", on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=30, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Transporter"
    









