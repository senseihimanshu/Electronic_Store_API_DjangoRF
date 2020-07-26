from rest_framework import permissions


class UpdateOwnProduct(permissions.BasePermission):
    """Allow user to edit their own products"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own product"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user.id == request.user.id
