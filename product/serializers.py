from rest_framework import serializers
from .models import Product
from django.conf import settings


class ProductSerializer(serializers.Serializer):
    user = serializers.RelatedField(settings.AUTH_USER_MODEL,
                                    on_delete=serializers.CASCADE)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)
    image = serializers.ImageField(
        upload_to=upload_product_image, null=True, blank=True)
    updated = serializers.DateTimeField()
    timestamp = serializers.DateTimeField()

    def create(self, validated_data):
        return Product.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.updated = validated_data.get('updated', instance.updated)
        instance.save()
        return instance
