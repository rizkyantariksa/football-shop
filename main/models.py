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
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False)
    brand = models.TextField(max_length=255)
    stock = models.IntegerField()
    
    def __str__(self):
        return self.title
