# Generated by Django 4.0.6 on 2022-07-13 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0003_alter_assessment_time_limit'),
    ]

    operations = [
        migrations.AddField(
            model_name='invite',
            name='message',
            field=models.TextField(blank=True, help_text='Add a message to the student', null=True),
        ),
    ]
