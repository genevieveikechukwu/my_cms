# Generated by Django 3.2.9 on 2022-07-26 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
    ]