from rest_framework import serializers
from .models import Bucket

class BucketSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Bucket
        fields = ('id', 'name', 'owner', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
