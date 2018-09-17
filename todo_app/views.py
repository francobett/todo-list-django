from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, TaskState, Priority
from .form import TaskForm


def todo_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo_list.html', {'tasks': tasks})


def edit_task(request, id=None, template_name='edit_task.html'):
    if id:
        task = get_object_or_404(Task, pk=id)
    else:
        task = Task(state=TaskState.objects.get(name='TODO'))

    form = TaskForm(request.POST or None, instance=task)
    if request.POST and form.is_valid():
        form.save()

        # Save was successful, so redirect to another page
        return redirect('todo_list')

    return render(request, template_name, {
        'form': form
    })


def delete_task(request, id=None):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    return redirect('todo_list')


def change_task_state(request, id=None):
    task = get_object_or_404(Task, pk=id)
    if task.state.name == 'TODO':
        # task.state == TaskState.objects.get(name='DONE')
        Task.objects.filter(pk=id).update(state=TaskState.objects.get(name='DONE'))
    elif task.state.name == 'DONE':
        # task.state == TaskState.objects.get(name='TODO')
        Task.objects.filter(pk=id).update(state=TaskState.objects.get(name='TODO'))
    return redirect('todo_list')
