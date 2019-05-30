import time

from celery import Celery


app = Celery(
    'tasks',
    broker='amqp://guest@rabbitmq//',
    backend='redis://redis',
)


@app.task
def add(x, y):
    if isinstance(x, str) or isinstance(y, str):
        return f'Received two strings {x} and {y}'
    return x + y


@app.task(bind=True)
def hello(self, a, b):
    time.sleep(1)
    self.update_state(state="PROGRESS", meta={'progress': 50})
    time.sleep(2)
    self.update_state(state="PROGRESS", meta={'progress': 90})
    time.sleep(3)
    return 'hello world: {}'.format(a + b)
