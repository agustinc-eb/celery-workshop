from celery import Celery


app = Celery(
    'tasks',
    broker='amqp://guest@rabbitmq//',
    backend='redis://redis',
)


@app.task
def add(x, y):
    return x + y
