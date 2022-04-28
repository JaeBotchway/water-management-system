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
    department=models.CharField(max_length=255, blank=True, null=True)
    address=models.CharField(max_length=255, blank=True, null=True)
    starting_date=models.DateField(auto_now=True)
    salary=models.DecimalField(max_digits=10, decimal_places=2, null=True)
    
    def __str__(self):
        return str(self.first_name)
       
    
    
class NextOfkin(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)  
    first_name=models.CharField(max_length=255, blank=True, null=True)
    last_name=models.CharField(max_length=255, blank=True, null=True)  
    phone_number=models.CharField(max_length=20)
    
    def __str__(self):
        return str(self.first_name)