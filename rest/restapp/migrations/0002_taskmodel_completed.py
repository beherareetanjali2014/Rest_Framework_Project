# Generated by Django 3.0.2 on 2020-01-15 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]