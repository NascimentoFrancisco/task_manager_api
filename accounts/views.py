from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.password_validation import validate_password
from rest_framework.permissions import IsAuthenticated

from accounts.models import User
from .accounts_serializer import (
    UserSerializer, CreateUserSerializer, ChangePasswordSerializer
)


class UserCreateViewApi(generics.CreateAPIView):
    """
    EndPoint that allows creating a new user in the system.
    """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    """
    EndPoint that allows changing an already registered user, requiring authentication.
    """
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_object(self):
        return self.request.user

    def perform_update(self, serializer):
        serializer.save()

class UserDeleteAPIView(generics.DestroyAPIView):
    """
    EndPoint que permite apagar um usuário já existente no sistema, necessário autenticação.
    """
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class ChangePasswordUserView(generics.UpdateAPIView):
    """
    EndPoint that allows deleting an existing user in the system, requiring authentication.
    """    
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj
    
    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Senha errada."]}, status=status.HTTP_400_BAD_REQUEST)
            
            validate_password(serializer.data.get("new_password"))
            
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()

            return Response("Senha alterada com sucesso.", status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)