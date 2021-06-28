from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
 
class CustomUser(AbstractUser):
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    username= models.CharField(blank=True, max_length=254,)
    email = models.EmailField(blank=False, max_length=254, unique=True, verbose_name="email address")