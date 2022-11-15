"""
docker run -d --hostname myrabbit --name myrabbit -p 5672:5672 rabbitmq:3

celery -A test_worker worker -l info
"""
import time

from celery import Celery, shared_task
from celery.utils.log import task_logger, worker_logger

app = Celery('tasks', broker='pyamqp://guest@localhost//', backend="rpc://")


@app.task
def add(x, y):
    task_logger.info("Add %s + %s = %s", x, y, x + y)
    return x + y


@shared_task(bind=True)
def sleep(self, seconds):
    """
    1초마다 자신 상태 정보를 변화시키는 시키는 비동기 task
    """

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

        worker_logger.info("This is worker_logger")
        task_logger.info("This is task_logger")

    return result
