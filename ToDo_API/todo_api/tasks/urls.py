from django.urls import path

from .views import ListTask, DetailTask, CreateTask


urlpatterns = [
    path('tasks/', ListTask.as_view()),
    path('tasks/<int:pk>/', DetailTask.as_view()),
    path('tasks/create', CreateTask.as_view())
]
