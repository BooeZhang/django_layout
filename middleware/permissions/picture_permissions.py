from rest_framework.permissions import BasePermission


class PicturePermissions(BasePermission):
    """
    自定义权限
    """

    def has_permission(self, request, view):
        if request.user == 'AnonymousUser':
            print('======')