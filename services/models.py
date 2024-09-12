
from django.db import models

class Service(models.Model):
    CATEGORY_CHOICES = [
        ('medical', 'Medical'),
        ('food', 'Food'),
        ('education', 'Education'),
        # Add more categories as needed
    ]

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    location = models.CharField(max_length=255)
    description = models.TextField()
    contact_info = models.CharField(max_length=255)
    hours = models.CharField(max_length=255)

    def __str__(self):
        return self.name
