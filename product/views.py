from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

# Inside ProductViewSet


# @action(methods=['POST'], default=True, url_path='upload-image')
# def upload_image(self, request, pk=None):
#     """Upload an image to product"""
#     product = self.get_object()
#     serializer = self.get_serializer(
#         product,
#         data=request.data
#     )

#     if serializer.is_valid():
#         serializer.save()
#         return Response(
#             serializer.data,
#             status=status.HTTP_200_OK
#         )

#     return Response(
#         serializer.errors,
#         status=status.HTTP_400_BAD_REQUEST
#     )
