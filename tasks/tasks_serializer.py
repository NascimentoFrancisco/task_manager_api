from rest_framework import serializers

from accounts.accounts_serializer import UserSerializer
from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    
    
    id = serializers.IntegerField(read_only=True)
    user = UserSerializer(read_only=True)
    status = serializers.BooleanField(read_only=True)
    punctuality = serializers.BooleanField(read_only=True)
    creation_date = serializers.DateTimeField(read_only=True)
    date_conclusion = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Task
        fields = (
            'id', 'user','title', 'description', 'creation_date',
            'deadline_date', 'date_conclusion', 'status', 'punctuality',
        )
        

class TaskFinishSerializer(serializers.ModelSerializer):
    

    id = serializers.IntegerField(read_only=True)
    user = UserSerializer(read_only=True)
    title = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    status = serializers.BooleanField(read_only=True)
    creation_date = serializers.DateTimeField(read_only=True)
    deadline_date = serializers.DateTimeField(read_only=True)
    date_conclusion = serializers.DateTimeField(read_only=True)
    punctuality = serializers.BooleanField(read_only=True)

    class Meta:

        model = Task
        fields = (
            'id', 'user','title', 'description', 'creation_date',
            'deadline_date', 'date_conclusion', 'status', 'punctuality',
        )
       