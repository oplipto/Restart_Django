from django.db import models
from django.utils import timezone

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


    def __str__(self):
        return self.name