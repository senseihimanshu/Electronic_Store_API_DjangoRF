from rest_framework import serializers
from django.conf import settings

from product import models


class ProductSerializer(serializers.ModelSerializer):
    """Serializes product items"""

    class Meta:
        model = models.Product
        fields = ('id', 'user', 'name', 'description',
                  'product_type', 'image', 'created_on')
        extra_kwargs = {'user': {'read_only': True}}


class ProductImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading images to products"""

    class Meta:
        model = models.Product
        fields = ('id', 'image')
        read_only_field = ('id',)


class MobileSerializer(serializers.ModelSerializer):
    """Serializes mobile items"""

    class Meta:
        model = models.Mobile
        fields = ('id', 'product', 'processor', 'ram',
                  'screen_size', 'color')
        extra_kwargs = {'product': {'read_only': True}}


class LaptopSerializer(serializers.ModelSerializer):
    """Serializes laptop items"""

    class Meta:
        model = models.Laptop
        fields = ('id', 'product', 'processor', 'ram',
                  'hd_capacity')
        extra_kwargs = {'product': {'read_only': True}}
