from rest_framework.permissions import BasePermission

class IsApproved(BasePermission):
    """
    Allows access only to "is_active" users.
    """
    def has_permission(self, request, view):
        return request.user and request.user.account.is_accepted
