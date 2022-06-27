from django.db import models
from django.contrib.auth.models import User


YEAR_IN_SCHOOL_CHOICES = (
    ('TO_DO', 'to-do'),
    ('IN_PROGRESS', 'In progress'),
    ('COMPLETED', 'completed'),
)


class Task(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    status = models.CharField(max_length=25, choices=YEAR_IN_SCHOOL_CHOICES, default='PENDING')
    creation_date = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='tasks')

    def __str__(self):
        return self.title
