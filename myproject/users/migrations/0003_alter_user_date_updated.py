# Generated by Django 4.1.1 on 2022-09-10 13:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_register_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
