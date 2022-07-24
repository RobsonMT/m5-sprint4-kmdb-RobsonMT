from rest_framework.permissions import BasePermission
from rest_framework.views import Request


class UserPermission(BasePermission):
    def has_permission(self, request: Request, _):

        print("\n\n", request.user, "\n\n")
        print("\n\n", request.method, "\n\n")

        superuser_methods = {
            "GET",
        }

        if request.method in superuser_methods:
            return request.user.is_superuser

        return True
