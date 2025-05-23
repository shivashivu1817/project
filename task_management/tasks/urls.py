from django.urls import path
from .views import TaskListCreate, TaskRetrieveUpdateDestroy
from .views import RegisterView
from .views import UserInfoView

urlpatterns = [

    path('user-info/', UserInfoView.as_view(), name='user-info'),

    path('tasks/', TaskListCreate.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroy.as_view(), name='task-detail'),
    path('register/', RegisterView.as_view(), name='register'),
]
