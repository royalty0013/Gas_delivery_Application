from django.db import models
import jsonfield
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
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

class Purchase(models.Model):
    customer_id = models.ForeignKey(User, related_name="Customer_account", on_delete=models.CASCADE)
    items_purchased = models.JSONField()
    price = models.FloatField()
    vendor_id = models.ForeignKey(User, related_name="Vendor", on_delete=models.CASCADE) 
    vendor_completed = models.BooleanField(default=False)
    transporter_completed = models.BooleanField(default=False)
    customer_completed = models.BooleanField(default=False)
    total_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Purchase Records"

class Transaction(models.Model):
    customer_id = models.ForeignKey(User, related_name="Customer_name", on_delete=models.CASCADE)
    transporter_id = models.ForeignKey(User, related_name="delivery_guy", on_delete=models.CASCADE)
    vendor_id = models.ForeignKey(User, related_name="Vendor_name", on_delete=models.CASCADE)
    transaction_completed = models.BooleanField(default=False)
    transaction_verified = models.BooleanField(default=False)
    Reference_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Transaction Records"






