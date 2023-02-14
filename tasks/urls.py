from django.urls import path

from .views import (
    TaskCreateAPIView, TaskUpdateAPIView,
    TaskDeleteAPIView, TaskFinishAPIView, TaskListAPIView
)

app_name = "api_tasks"


urlpatterns = [
    path('create/', TaskCreateAPIView.as_view(), name='create_tastk_api'),
    path('list/', TaskListAPIView.as_view(), name='create_tastk_api'),
    path('update/<int:id>/', TaskUpdateAPIView.as_view(), name='update_tastk_api'),
    path('delete/<int:id>/', TaskDeleteAPIView.as_view(), name='delete_tastk_api'),
    path('finish/<int:id>/', TaskFinishAPIView.as_view(), name='finish_tastk_api'),
]