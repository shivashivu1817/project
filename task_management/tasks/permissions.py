from rest_framework import permissions

class IsAdminOrOwner(permissions.BasePermission):
    """
    Admins can access all tasks. Regular users can access only their own.
    """

    def has_object_permission(self, request, view, obj):
        if request.user.profile.role == 'ADMIN':
            return True
        return obj.owner == request.user

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
