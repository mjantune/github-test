# Generated by Django 2.1.7 on 2019-03-21 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='content',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='summary',
        ),
    ]
