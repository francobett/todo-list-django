from django import forms
from .models import Task, TaskState, Priority


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('name', 'description', 'priority',)
