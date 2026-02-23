from rest_framework import serializers
from .models import Tasks


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id', 'title', 'description', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
