from rest_framework import serializers
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    

    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        help_text='A short name for your unique identification in the system.'
    )
    name = serializers.CharField(
        help_text='Your name, preferably your full name.'
    )
    email = serializers.EmailField(
        help_text = 'A valid email for sending notifications if necessary.'
    )
    is_active = serializers.BooleanField(read_only=True)
    is_staff = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = (
            'id','username', 'name', 'email', 'is_active','is_staff',
        )


class CreateUserSerializer(serializers.ModelSerializer):
    

    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        help_text='A short name for your unique identification in the system.'
    )
    name = serializers.CharField(
        help_text='Your name, preferably your full name.'
    )
    email = serializers.EmailField(
        help_text = 'A valid email for sending notifications if necessary.'
    )
    password = serializers.CharField(write_only=True,
        help_text="""
            Your password cannot be too similar to the rest of your personal information, 
            it must be at least 8 characters long and cannot be entirely numerical.
        """
    )

    class Meta:
        model = User
        fields = ['id','username', 'name', 'email', 'password']
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class ChangePasswordSerializer(serializers.Serializer):
    

    old_password = serializers.CharField(required=True, 
        help_text='Current password.'
    )
    new_password = serializers.CharField(required=True, 
        help_text='New Password.'
    )