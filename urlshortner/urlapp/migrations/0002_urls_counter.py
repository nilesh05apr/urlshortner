# Generated by Django 4.0.5 on 2022-07-05 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='urls',
            name='counter',
            field=models.IntegerField(default=1),
        ),
    ]