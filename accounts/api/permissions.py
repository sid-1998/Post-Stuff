from rest_framework import permissions

class AnonPermissionOnly(permissions.BasePermission):
    message = "You are already logged in. Please log out to try again."

    def has_permission(self, request, view):
        return not request.user.is_authenticated


class IsOwnerOrReadOnly(permissions.BasePermission):
    message = "You should be the owner of the post to edit/delete it."

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user # checking of owner of the post and the one who is editing is same or not