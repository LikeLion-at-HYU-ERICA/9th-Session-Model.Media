# Generated by Django 3.2 on 2021-05-21 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0012_blog_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='image',
        ),
    ]
