from django.contrib import admin
from .models import Priority, TaskState, Task

admin.site.register(Priority)
admin.site.register(TaskState)
admin.site.register(Task)
