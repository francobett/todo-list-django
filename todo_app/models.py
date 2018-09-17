from django.db import models
from django.utils import timezone

# Create your models here.


class Priority(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class TaskState(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    # create_at = models.DateTimeField(default=timezone.now)
    priority = models.ForeignKey(Priority, default='LOW')
    state = models.ForeignKey(TaskState, default='TODO')

    def __str__(self):
        return self.name
