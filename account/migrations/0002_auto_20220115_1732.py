# Generated by Django 3.2 on 2022-01-15 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='userlogin',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]