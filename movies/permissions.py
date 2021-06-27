from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):

        message = "You do not have permission to perform this action."

        if request.user._wrapped.is_admin or request.method in SAFE_METHODS:
            return True
