# Generated by Django 3.2.4 on 2021-06-04 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_auto_20210604_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='hall',
        ),
    ]
