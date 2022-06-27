from django.urls import path

from .views import ListTask, DetailTask, CreateTask


urlpatterns = [
    path('', ListTask.as_view()),
    path('<int:pk>/', DetailTask.as_view()),
    path('create', CreateTask.as_view())
]
