from django.db import models
from user.models import User
# Create your models here.

class Jwt(models.Model):
    user = models.OneToOneField(User, related_name='login_name', on_delete=models.CASCADE)
    access = models.TextField()
    refresh = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name_plural = "Tokens"
    
   

