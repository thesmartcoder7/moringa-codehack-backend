# Generated by Django 4.0.6 on 2022-07-13 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='time_limit',
            field=models.PositiveIntegerField(blank=True, help_text='Duration of assessment in minutes'),
        ),
    ]
