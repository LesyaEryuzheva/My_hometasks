from django.db import models
from django.contrib.auth.models import User


TASK_STATUS_CHOICES = (
    ('TO_DO', 'To do'),
    ('IN_PROGRESS', 'In progress'),
    ('COMPLETED', 'Completed'),
)


class Task(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    status = models.CharField(max_length=25, choices=TASK_STATUS_CHOICES, default='TO_DO')
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title
