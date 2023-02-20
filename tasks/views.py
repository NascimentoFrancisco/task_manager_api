from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from .tasks_serializer import TaskSerializer, TaskFinishSerializer
from tasks.models import Task


class TaskCreateAPIView(generics.CreateAPIView):
    """
    EndPoint for creating tasks for a user who is logged in.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskListAPIView(generics.ListAPIView):
    """
    EndPoint that lists the logged in user's tasks.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    
    def get_queryset(self):

        queryset = Task.objects.filter(user=self.request.user)
        return queryset

class TaskUpdateAPIView(generics.UpdateAPIView):
    """
    Endpoint that updates a task that the user passes the id parameter, authentication required.
    """
    permission_classes = [IsAuthenticated]

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'


class TaskStartAPIView(generics.UpdateAPIView):

    permission_classes = [IsAuthenticated]

    queryset = Task.objects.all()
    serializer_class = TaskFinishSerializer
    lookup_field = 'id'

    def perform_update(self, serializer):
        
        now = timezone.now()

        serializer.save(
            startup_date = now,
            start_task = True,
        )



class TaskFinishAPIView(generics.UpdateAPIView):
    """
    EndPoint that updates the status of a task that the user passes the id parameter, 
    authentication required.
    """
    permission_classes = [IsAuthenticated]

    queryset = Task.objects.all()
    serializer_class = TaskFinishSerializer
    lookup_field = 'id'

    def perform_update(self, serializer):
        
        now = timezone.now()
        punctuality = False
        
        if now <= self.get_object().deadline_date:
            punctuality = True

        serializer.save(
            date_conclusion = now,
            status = True,
            punctuality = punctuality
        )

class TaskDeleteAPIView(generics.DestroyAPIView):
    """
    Endpoint that deletes a task that the user passes the id parameter, authentication required.
    """
    permission_classes = [IsAuthenticated]

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'