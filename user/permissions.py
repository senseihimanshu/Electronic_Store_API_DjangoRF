from rest_framework import permissions


class UpdateOwnCredentials(permissions.BasePermission):
    """Allow user to edit their own credentials"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own credential"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
