from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.todo_list, name='todo_list'),  # '/' Url sin parametros
    url(r'^task/new/$', views.edit_task, name='new_task'),  # '/new'
    url(r'^task/(?P<id>[0-9]+)/$', views.edit_task, name='edit_task'),
    url(r'^task/delete/(?P<id>[0-9]+)/$', views.delete_task, name='delete_task'),
    url(r'^task/change/(?P<id>[0-9]+)/$', views.change_task_state, name='change_task_state'),
]
