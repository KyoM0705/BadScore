# Generated by Django 2.2 on 2019-05-06 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=100)),
                ('leftLeft', models.CharField(max_length=100)),
                ('leftRight', models.CharField(max_length=100)),
                ('rightLeft', models.CharField(max_length=100)),
                ('rightRight', models.CharField(max_length=100)),
            ],
        ),
    ]
