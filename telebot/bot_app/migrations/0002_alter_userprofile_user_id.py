# Generated by Django 4.1.2 on 2022-12-11 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_id',
            field=models.PositiveIntegerField(unique=True, verbose_name='User Telegram ID'),
        ),
    ]
