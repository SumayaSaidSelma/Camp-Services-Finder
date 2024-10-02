from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.files.storage import FileSystemStorage


fs = FileSystemStorage(location='/media/photos')

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Service(models.Model):
    CATEGORY_CHOICES = [
        ('medical', 'Medical'),  
        ('medical_ar', 'طبي'),   
        ('food', 'Food'),       
        ('food_ar', 'طعام'),     
        ('education', 'Education'),  
        ('education_ar', 'تعليم'),   
        ('other', 'Other'),      
        ('other_ar', 'آخر'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    location = models.CharField(max_length=100)
    description = models.TextField()
    contact_info = models.CharField(max_length=100)
    hours = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name
