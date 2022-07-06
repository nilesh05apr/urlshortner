# Generated by Django 4.0.5 on 2022-07-06 19:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('urlapp', '0002_urls_counter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='id',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=12, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='urls',
            name='long_url',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='urls',
            name='short_url',
            field=models.CharField(max_length=10),
        ),
    ]