from celery import shared_task
from time import sleep

### Programatically Scheduelr krne ke lie

from django_celery_beat.models import PeriodicTask,IntervalSchedule
import json


@shared_task
def sub(x,y):
    sleep(40)
    return x-y



### For Periodic Task 
@shared_task
def clear_session_cache(id):
    print(f"Session Cache Cleared:  {id}")
    return id

@shared_task
def clear_redis_data(key):
    print(f"Redis Data Cleared :{key}")
    return key


@shared_task()
def clear_rabbitmq_data(key):
    print(f"RabbitMQ Data Cleared : {key}")
    return key


### Create Schedule that run every 30 seconds

schedule,created=IntervalSchedule.objects.get_or_create(
    every=30,
    period=IntervalSchedule.SECONDS
)

#Schedule the periodic task programattically

PeriodicTask.objects.get_or_create(
    name='Clear RabbitMQ Periodic Task',
    task='app.tasks.clear_rabbitmq_data',
    interval=schedule,
    args=json.dumps(["Hello Amar"]) #Pass the arguments to task as a JSON-encoded list
)