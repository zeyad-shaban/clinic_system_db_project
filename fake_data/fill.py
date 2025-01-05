# python manage.py shell

from django.db import connection

with open('fake_data/insert.sql', 'r') as file:
    sql = file.read()
    with connection.cursor() as cursor:
        cursor.executescript(sql)