'''
we can write our permissions in hear
'''
from rest_framework.permissions import BasePermission

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
PERMS_MAP = {
    'GET': 'view_',
    'DELETE': 'delete_',
    'PATCH': 'change_',
    'POST': 'add_',
    'PUT': 'change_'
}


# in hear i test how can write base on default IsAuthenticatedOrReadOnly
class IsAddressOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        """
        for list
        Return `True` if permission is granted, `False` otherwise.
        """
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        """
        for detail
        Return `True` if permission is granted, `False` otherwise.
        """
        return bool(
            request.method in SAFE_METHODS or
            request.user == obj.user
            # user is owner of Address
            or request.user.is_staff
        )


# class UserViewPermissions_B(BasePermission):
#     def has_permission(self, request, view):
#         app_label = view.queryset.model._meta.app_label
#         model_name = view.queryset.model._meta.model_name
#
#         if request.method in SAFE_METHODS:
#             return True
#         elif request.method == 'POST':
#             return request.user.is_superuser or not request.user.is_authenticated
#         elif request.method in ('PUT', 'PATCH'):
#             return request.user.has_perm(str(app_label+'.'+PERMS_MAP[request.method]+model_name)) or \
#                    request.user.is_superuser
#         elif request.method == 'DELETE':
#             return request.user.has_perm(str(app_label+'.'+PERMS_MAP[request.method]+model_name)) or \
#                    request.user.is_superuser
#         return False
#
#     def has_object_permission(self, request, view, obj):
#         return obj.email == request.user.email or \
#                request.user.is_superuser

#
#
# thsi is the best way
class UserViewPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.method == 'POST':
            return request.user.is_superuser or not request.user.is_authenticated
        elif request.method in ('PUT', 'PATCH'):
            return request.user.is_superuser or request.user.is_authenticated
        elif request.method == 'DELETE':
            return request.user.is_superuser or request.user.is_authenticated
        return False

    def has_object_permission(self, request, view, obj):
        return obj.email == request.user.email or \
               request.user.is_superuser

class SuperUserPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method: #  == ('GET', 'HEAD', 'OPTIONS', 'POST', 'PUT', 'PATCH', 'DELETE')
            return request.user.is_superuser
        return False

    def has_object_permission(self, request, view, obj):
        return obj.email == request.user.email or request.user.is_superuser


class ShopPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.method == 'POST':
            return request.user.is_authenticated

        elif request.method in ('PUT', 'PATCH', 'DELETE'):
            return request.user.is_authenticated

        return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        if request.method in ('PUT', 'PATCH', 'DELETE'):
            return request.user.is_superuser or obj.user == request.user

        return False