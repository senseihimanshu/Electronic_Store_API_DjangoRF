from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from product import serializers
from product import models
from product import permissions


class ProductViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, and updating products"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    permission_classes = (
        permissions.UpdateOwnProduct,
        IsAuthenticated
    )

    def perform_create(self, serializer):
        """Sets the product to the logged in user"""
        serializer.save(user=self.request.user)

    @action(methods=['POST'], detail=True, url_path='upload-image')
    def upload_image(self, request, pk=None):
        """Upload an image to product"""
        product = self.get_object()
        serializer_class = serializers.ProductImageSerializer

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
