# Generated by Django 2.2 on 2019-05-07 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badApp', '0002_auto_20190506_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='server',
            field=models.CharField(default='', max_length=100),
        ),
    ]
