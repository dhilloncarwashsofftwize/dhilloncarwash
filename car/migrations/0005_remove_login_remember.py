# Generated by Django 2.0 on 2020-03-19 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0004_auto_20200319_1743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='remember',
        ),
    ]
