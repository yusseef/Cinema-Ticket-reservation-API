# Generated by Django 3.2.4 on 2021-06-05 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0006_auto_20210605_0417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='movie',
        ),
    ]
