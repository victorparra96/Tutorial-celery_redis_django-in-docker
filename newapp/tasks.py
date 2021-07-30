# Celery
from celery import shared_task
from celery.decorators import task
from celery.utils.log import get_task_logger

# Python
from random import randint

from .emails import send_review_email

logger = get_task_logger(__name__)

#@shared_task
@task(name="send_review_email_task")
def send_review_email_task(name, email, review):
    logger.info("Sent review email")
    return send_review_email(name, email, review)

@task(name="sum_random")
def sum_random():
    suma = lambda a, b: a + b
    c = randint(1,10)
    d = randint(1,10)
    print(suma(c, d))
