"""
docker run -d --hostname myrabbit --name myrabbit -p 5672:5672 rabbitmq:3

celery -A test_worker worker -l info
"""
import time

from celery import Celery, shared_task

app = Celery('tasks', broker='pyamqp://guest@localhost//', backend="rpc://")


@app.task
def add(x, y):
    return x + y


@shared_task(bind=True)
def sleep(self, seconds):
    result = 0
    for i in range(seconds):
        time.sleep(1)
        result += i

        # update progress
        if not self.request.called_directly:
            self.update_state(
                state='PROGRESS',
                meta={'current': i, 'total': seconds}
            )

    return result
