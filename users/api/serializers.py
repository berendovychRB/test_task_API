from rest_framework import serializers

from ..models import Group, User


class GroupSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)

    class Meta:
        model = Group
        fields = [
            'id', 'name', 'description'
        ]


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects)

    class Meta:
        model = User
        fields = [
            'id', 'username', 'group'
        ]