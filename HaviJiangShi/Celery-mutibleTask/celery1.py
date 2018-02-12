from celery import Celery#
app = Celery('tasks', broker='redis://:''@223.129.0.190:6379/2', backend='redis://:''@223.129.0.190:6379/3')

@app.task
def add(x, y):
    return x + y
