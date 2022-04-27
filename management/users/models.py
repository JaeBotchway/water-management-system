from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

CATEGORY_CHOICES =[
    ('admin', 'admin'),
    ('sales', 'sales'),
    ('production', 'production')
]


class User(AbstractUser):
    phone_number=models.CharField(max_length=20)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    password=models.CharField(max_length=10)
    role=models.CharField(choices=CATEGORY_CHOICES,
        max_length=10)