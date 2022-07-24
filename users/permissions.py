from rest_framework.permissions import BasePermission
from rest_framework.views import Request


class UserPermission(BasePermission):
    def has_permission(self, request: Request, _):

        superuser_methods = {
            "GET",
        }

        if request.method in superuser_methods:
            return request.user.is_superuser

        return True
