from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django import forms
from .models import models

# Create your models here.

class firstVariety(models.Model):
    FIRST_TYPE_CHOICES = (
        ('LG', 'Lamborghini'),
        ('FR', 'Ferrari'),
        ('BM', 'BMW'),
        ('AU', 'Audi'),
        ('MB', 'Mercedes Benz')
    )

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=FIRST_TYPE_CHOICES, default='LG')
    price_currency = models.CharField(max_length=1000, default='USD')
    description = models.TextField(default='')

    def __str__(self):
        return self.name
    
class firstVarietyReview(models.Model):
    firstvariety = models.ForeignKey(firstVariety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.firstvariety.name} - {self.user.username} - {self.rating}"
    
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    first_varieties = models.ManyToManyField(firstVariety, related_name='stores')

    def __str__(self):
        return self.name
    
class firstVarietyCertificate(models.Model):
    first = models.OneToOneField(firstVariety, on_delete=models.CASCADE, related_name='certificate')
    certifcate_number = models.CharField(max_length=100)
    date_issued = models.DateTimeField(default=timezone.now)
    date_expired = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Certificate for {self.first.name}"