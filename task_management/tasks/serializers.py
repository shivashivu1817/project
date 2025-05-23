from rest_framework import serializers
from .models import Task

from django.contrib.auth.models import User


class UserInfoSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source='profile.role')  # Assuming profile has a 'role'
    groups = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'groups']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['owner']