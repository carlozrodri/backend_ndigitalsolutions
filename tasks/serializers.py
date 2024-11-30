from rest_framework import serializers
from tasks.models import Task
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the Task model. Converts model instances to JSON and
    validates input data.
    """

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'created_at', 'updated_at']


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model to handle user-related operations.
    """

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    def create(self, validated_data: dict) -> User:
        """
        Create a new user with a hashed password.
        """
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
