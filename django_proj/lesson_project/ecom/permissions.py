import re
from rest_framework.permissions import BasePermission

class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.profile_id.user == request.user

    # def has_permission(self, request, view):
    #     return super().has_permission(request, view)