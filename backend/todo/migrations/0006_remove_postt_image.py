# Generated by Django 2.2.10 on 2020-08-16 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20200812_0844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postt',
            name='image',
        ),
    ]
