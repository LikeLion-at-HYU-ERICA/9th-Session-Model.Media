# Generated by Django 3.1.2 on 2021-05-20 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_auto_20210520_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='firstapp.category'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('comment_user', models.TextField(max_length=20)),
                ('comment_textfield', models.TextField()),
                ('blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='firstapp.blog')),
            ],
        ),
    ]