from django.utils.translation import gettext_lazy as _
from rest_framework.permissions import IsAuthenticated
from core.User.models import User


class AdminPermissions(IsAuthenticated):
    message = _('User has to be staff or superuser')

    def has_permission(self, request, view):
        parent_res = super().has_permission(request, view)
        if not parent_res:
            return False

        user: User = request.user
        return user and user.is_active and (user.is_staff or user.is_superuser)


class SuperuserPermissions(IsAuthenticated):
    message = _('User has to be superuser')

    def has_permission(self, request, view):
        parent_res = super().has_permission(request, view)
        if not parent_res:
            return False

        user: User = request.user
        return user and user.is_active and user.is_superuser
