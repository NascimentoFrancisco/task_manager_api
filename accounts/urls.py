from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from .views import (
    UserCreateViewApi, UserUpdateAPIView,
    UserDeleteAPIView, ChangePasswordUserView
)
""" from .tasks_viewssets import (
    TaskViewsSets, TaskCreateAPIView, TaskUpdateAPIView,
    TaskDeleteAPIView, TaskFinishAPIView, TaskListAPIView
) """


app_name = "api_accounts"


urlpatterns = [
    #path('',include(router.urls), name='api_accounts'),
    path('user/token/', TokenObtainPairView.as_view()),
    path('user/token/refresh/',TokenRefreshView.as_view()),
    path('user/create/', UserCreateViewApi.as_view(), name='create_user_api'),
    path('user/update/', UserUpdateAPIView.as_view(), name='update_user_api'),
    path('user/delete/', UserDeleteAPIView.as_view(), name='update_user_api'),
    path('user/change-password/', ChangePasswordUserView.as_view(), 
        name='update_user_api'
    ),
]

""" path('task/create/', TaskCreateAPIView.as_view(), name='create_tastk_api'),
    path('task/list/', TaskListAPIView.as_view(), name='create_tastk_api'),
    path('task/update/<int:id>/', TaskUpdateAPIView.as_view(), name='update_tastk_api'),
    path('task/delete/<int:id>/', TaskDeleteAPIView.as_view(), name='delete_tastk_api'),
    path('task/finish/<int:id>/', TaskFinishAPIView.as_view(), name='finish_tastk_api'), """