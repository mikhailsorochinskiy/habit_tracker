from rest_framework.permissions import BasePermission


class IsOwnerOrAdmin(BasePermission):
    """
    Разрешение, позволяющее редактировать объект только владельцу или админу.
    """
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj == request.user
