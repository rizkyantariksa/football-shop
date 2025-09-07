import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('sepatu', 'Sepatu'),
        ('bola', 'Bola'),
        ('jersey', 'Jersey'),
        ('aksesoris', 'Aksesoris'),
    ]

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='sepatu')
    is_featured = models.BooleanField(default=False)
    stock = models.IntegerField()
    brand = models.CharField(max_length=255)

    def __str__(self):
        return self.title