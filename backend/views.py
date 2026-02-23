from rest_framework import viewsets
from rest_framework.response import Response
from .models import Tasks
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """Skeletal TaskViewSet for CRUD operations."""
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

