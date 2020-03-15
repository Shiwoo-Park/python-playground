# Playground

## What's included

- Django & DRF
- Celery
- [Fluent Python] example codes

## My "play"ed list

### Celery progress bar with django
```shell script
# create rabbitmq as broker
docker run -d --hostname myrabbit --name myrabbit -p 5672:5672 rabbitmq:3

# run celery
celery -A test_worker worker -l info

# run django
python manage.py runserver 8000 
```
