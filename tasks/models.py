from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    """
    Represents a task that belongs to a user.

    Attributes:
        user (ForeignKey): The user who owns this task.
        title (str): A short title describing the task.
        description (str): A detailed description of the task.
        completed (bool): Indicates whether the task is completed.
        created_at (datetime): The timestamp when the task was created.
        updated_at (datetime): The timestamp when the task was last updated.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """
        String representation of the task.
        """
        return self.title
