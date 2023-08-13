from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("taskq2", views.taskq2, name="taskq2"),
    path("taskexec", views.taskexec, name="taskexec"),
    path("status/<str:task_id>", views.status, name="status"),
]
