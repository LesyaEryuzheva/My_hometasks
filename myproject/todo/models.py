from django.db import models


class Todo(models.Model):
    description = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return f'Todo {self.pk}. Date: {self.date}'