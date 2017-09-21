from rest_framework import serializers
from .models import Bucketlist


class BucketlistSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into JSON format"""

    class Meta:
        """Meta class to map serializer's fields with the model's fields"""
        model = Bucketlist
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
