Start celery:

python manage.py celeryd --setting=settings

Can also be started with

python manage.py supervisor


Kill celery processes if hung:

ps ax | grep celery | cut -b1-5 | xargs kill -9 

Rabbitmq setup:

rabbitmqctl add_user tester tester
rabbitmqctl add_vhost test_vhost
rabbitmqctl set_permissions -p test_vhost tester ".*" ".*" ".*"

Mysql:

database: test
user: root
password: [none]
