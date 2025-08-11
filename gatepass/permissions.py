from django.contrib.auth.models import Permission, User
from rest_framework import permissions

class IsAdminUser(permissions.BasePermission):
    """
    Custom permission to only allow admin users to access certain views.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the owner of the gate pass.
        return obj.owner == request.user

class CanApproveGatePass(permissions.BasePermission):
    """
    Custom permission to allow only users with the 'can_approve_gate_pass' permission to approve gate passes.
    """

    def has_permission(self, request, view):
        return request.user.has_perm('gatepass.can_approve_gate_pass')