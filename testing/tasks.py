from celery.task import task, periodic_task
from celery.schedules import crontab


import logging
logger = logging.getLogger(__name__)

@task
def do_something():
    print "Foo"
    logger.info('I am doing something')
    
@periodic_task(run_every=crontab(hour="*", minute="*", day_of_week="*"),options={"expires": 60*60})
def do_periodic():
    print "Bar"
    logger.info('I am a periodic task')

