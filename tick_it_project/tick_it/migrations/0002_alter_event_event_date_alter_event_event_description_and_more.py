# Generated by Django 4.2.3 on 2023-07-19 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tick_it', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_time',
            field=models.TimeField(),
        ),
    ]