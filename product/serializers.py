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
