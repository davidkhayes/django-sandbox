import os, platform, psutil, subprocess

from django_q.tasks import async_task, result, Task


command = r"bin\task.bat" if platform.system() == "Windows" else r"bin/task.sh"


def spawner():
    subprocess.call([command])


def run_taskq2():
    task_id = async_task("utils.utils.spawner", hook="utils.utils.print_result")
    return task_id


def run_taskexec():
    process = subprocess.Popen(
        [command],
        shell=False,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        close_fds=True,
    )
    return process.pid


def print_result(task):
    print(task.result)


def get_status(task_id):
    if task_id is None:
        return None

    if len(task_id) == 32:  # q2 task
        result = Task.objects.filter(id=task_id).values_list("success")

        if result.count() == 0:
            return "running"

        if result.count() > 1:
            return "huh?"

        if result[0][0] == True:
            return "finished"
        else:
            return "failed"

    else:  # exec task
        p = psutil.Process(int(task_id))
        print(p)
        if p:
            if p.status() == "running":
                return "running"
            if p.status() == "zombie":
                os.waitpid(int(task_id), 0)
                return "finished"
        return "unknown"
