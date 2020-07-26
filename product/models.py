import uuid
import os

from django.db import models
from django.conf import settings


def product_image_file_path(instance, filename):
    """Generate file path for new product image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return '/'.join(['uploads/product/', filename])


class Product(models.Model):
    """Product model"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=52)
    description = models.CharField(max_length=255)
    image = models.ImageField(null=True, upload_to=product_image_file_path)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return self.name


class Mobile(models.Model):
    """Mobile model"""
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    processor = models.CharField(max_length=42)
    ram = models.CharField(max_length=12)
    screen_size = models.CharField(max_length=24)
    color = models.CharField(max_length=22)

    def __str__(self):
        """Return the model as a string"""
        return self.product


class Laptop(models.Model):
    """Laptop model"""
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    processor = models.CharField(max_length=42)
    ram = models.CharField(max_length=12)
    hd_capacity = models.CharField(max_length=18)

    def __str__(self):
        """Return the model as a string"""
        return self.product
