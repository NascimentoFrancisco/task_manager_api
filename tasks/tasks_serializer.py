from rest_framework import serializers
from django.utils import timezone

from accounts.accounts_serializer import UserSerializer
from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    
    
    id = serializers.IntegerField(read_only=True)
    user = UserSerializer(read_only=True)
    title = serializers.CharField(
        help_text='General title of the task.'
    )
    description =  serializers.CharField(
        help_text='Text that explains more details about the task.'        
    )
    start_date_task = serializers.DateTimeField(
        help_text='Date/time when the task will start running. In YYYY-MM-DD hh:mm format.'
    )
    deadline_date = serializers.DateTimeField(
        help_text='Task expiration date/time. In YYYY-MM-DD hh:mm format.'
    )
    startup_date = serializers.DateTimeField(read_only=True)
    status = serializers.BooleanField(read_only=True)
    punctuality = serializers.BooleanField(read_only=True)
    creation_date = serializers.DateTimeField(read_only=True)
    date_conclusion = serializers.DateTimeField(read_only=True)
    start_task = serializers.BooleanField(read_only=True)

    class Meta:
        model = Task
        fields = (
            'id', 'user','title', 'description', 'start_date_task',
            'creation_date', 'deadline_date', 'startup_date','date_conclusion', 
            'status', 'punctuality', 'start_task',
        )
    
    def validate(self, attrs):
        
        if attrs['start_date_task'] == attrs['deadline_date']:
            raise serializers.ValidationError(
                {"start_date_task": "Data/hora de inicio e Data/hora prazo não podem ser iguais."}
            )
        
        if attrs['deadline_date'] < timezone.now():
            raise serializers.ValidationError(
                {"deadline_date": "Essa data/hora não pode ser em um periódo já ultrapassada!"}
            )
        elif  attrs['start_date_task'] < timezone.now():
            raise serializers.ValidationError(
                {"start_date_task": "Essa data/hora não pode ser em um periódo já ultrapassada!"}
            )

        return super().validate(attrs)
        

class TaskFinishSerializer(serializers.ModelSerializer):
    

    id = serializers.IntegerField(read_only=True)
    user = UserSerializer(read_only=True)
    title = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    start_date_task = serializers.DateTimeField(read_only=True)
    status = serializers.BooleanField(read_only=True)
    creation_date = serializers.DateTimeField(read_only=True)
    deadline_date = serializers.DateTimeField(read_only=True)
    startup_date = serializers.DateTimeField(read_only=True)
    date_conclusion = serializers.DateTimeField(read_only=True)
    punctuality = serializers.BooleanField(read_only=True)
    start_task = serializers.BooleanField(read_only=True)

    class Meta:

        model = Task
        fields = (
            'id', 'user','title', 'description', 'creation_date',
            'start_date_task','deadline_date', 'date_conclusion', 
            'startup_date','status', 'punctuality', 'start_task'
        )
       