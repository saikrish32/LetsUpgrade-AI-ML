# Generated by Django 3.1.1 on 2020-09-26 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_auto_20200926_2105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friends',
            name='Rollno',
        ),
        migrations.AddField(
            model_name='friends',
            name='secret_friend',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
