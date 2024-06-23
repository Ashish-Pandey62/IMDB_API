from rest_framework import permissions
from rest_framework.permissions import BasePermission, IsAuthenticated

class AdminOrReadOnly(permissions.IsAdminUser) :
    def has_permission(self,request,view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff) 
     
class ReviewUserorReadOnly(permissions.BasePermission):
    def has_permission(self,request,view,obj):
       if request.method in permissions.SAFE_METHODS:
        # Check permissions for read-only request
        return True
       else:
        # Check permissions for write request
        return object.review_user == request.user
        