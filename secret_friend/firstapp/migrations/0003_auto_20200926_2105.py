# Generated by Django 3.1.1 on 2020-09-26 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='friends',
            name='Choice_1',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='friends',
            name='Hint2',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='friends',
            name='challenge',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
    ]
