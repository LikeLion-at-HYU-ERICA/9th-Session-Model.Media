# Generated by Django 3.1.2 on 2021-05-20 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_auto_20210520_2306'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_textfield',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comment_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comment_user',
            new_name='user',
        ),
    ]
