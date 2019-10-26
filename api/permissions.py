from rest_framework.permissions import BasePermission
from .models import Bucket

class IsOwner(BasePermission):
    """Custom permission class to allow only bucketlist owners to edit them."""
    
    def has_object_permission(self, request, view, object):
        """Return True if permission is granted to the bucket owner."""
        if isinstance(object, Bucket):
            return object.owner == request.user
        return object.owner == request.user
