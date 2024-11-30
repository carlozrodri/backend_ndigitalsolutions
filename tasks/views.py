from rest_framework import generics
from tasks.models import Task
from tasks.serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated


class TaskListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    """
    API view to list and create tasks for the authenticated user.
    """
    serializer_class = TaskSerializer

    def get_queryset(self):
        """
        Return tasks that belong to the authenticated user.
        """
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Automatically associate the created task with the authenticated user.
        """
        serializer.save(user=self.request.user)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a specific task.
    """
    serializer_class = TaskSerializer

    def get_queryset(self):
        """
        Return the specific task for the authenticated user.
        """
        return Task.objects.filter(user=self.request.user)
