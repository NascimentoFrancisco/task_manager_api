from rest_framework import serializers
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    

    id = serializers.IntegerField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    is_staff = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = (
            'id','username', 'name', 'email', 'is_active','is_staff',
        )


class CreateUserSerializer(serializers.ModelSerializer):
    

    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id','username', 'name', 'email', 'password']
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ChangePasswordSerializer(serializers.Serializer):
    

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)