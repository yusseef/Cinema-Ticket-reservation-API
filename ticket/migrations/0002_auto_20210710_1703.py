# Generated by Django 3.2.4 on 2021-07-10 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='hall',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='uid',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='uid',
        ),
    ]
