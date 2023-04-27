from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):

    profile_image = models.FileField(
        upload_to = 'profile_image/' 
    )
    
    USER_STATUS = (
        ('usual','usual'),
        ('pro','pro'),
        ('admin','admin')
    )
    
    user_status = models.CharField(
        max_length=50,
        choices = USER_STATUS
        )
    email = models.EmailField(
        max_length=50,
        blank = True,
        null = True
        )