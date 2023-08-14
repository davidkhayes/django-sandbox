from utils.utils import get_status, run_taskq2, run_taskexec

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

import time

from utils.utils import is_positive_integer

def index(request):
    t = str(time.time())
    person = "david"
    context = {}
    return render(request, "testapp/index.html", context)


def taskq2(request):
    if request.method == "POST":
        if request.POST["count"] and is_positive_integer(request.POST["count"]):
            count = int(request.POST["count"])
        else:
            count = 10
        task_id = run_taskq2(count)
        context = {"task_id": task_id}
        return render(request, "testapp/task.html", context)

    if request.method == "GET":
        context = {"task_id": None}
        return render(request, "testapp/task.html", context)

def taskexec(request):
    if request.method == "POST":
        if request.POST["count"] and is_positive_integer(request.POST["count"]):
            count = int(request.POST["count"])
        else:
            count = 10
        task_id = run_taskexec(count)
        context = {"task_id": task_id}
        return render(request, "testapp/task.html", context)

    if request.method == "GET":
        context = {"task_id": None}
        return render(request, "testapp/task.html", context)

def status(request, task_id=None):
    status = get_status(task_id)
    return JsonResponse({"status": status})

