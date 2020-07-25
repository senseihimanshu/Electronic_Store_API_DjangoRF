from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from user import serializers
from user import models
from user import permissions


class UserView(APIView):
    """Test API View"""
    serializers_class = serializers.UserSerializer

    def get(self, request, format=None):
        """Returns a list of API View features"""
        return Response({'message': 'Working'})

    def post(self, request):
        serializer = self.serializers_class(data=request.data)

        if serializer.is_valid():
            message = 'Yippee'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class UserViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnCredentials,)
