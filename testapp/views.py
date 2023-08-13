from utils.utils import get_status, run_taskq2, run_taskexec

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

import time


def index(request):
    t = str(time.time())
    person = "david"
    context = {}
    return render(request, "testapp/index.html", context)


def taskq2(request):
    task_id = run_taskq2()
    context = {"task_id": task_id}
    return render(request, "testapp/task.html", context)


def taskexec(request):
    task_id = run_taskexec()
    context = {"task_id": task_id}
    return render(request, "testapp/task.html", context)


def status(request, task_id=None):
    status = get_status(task_id)
    return JsonResponse({"status": status})

