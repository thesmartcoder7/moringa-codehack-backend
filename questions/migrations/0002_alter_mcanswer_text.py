# Generated by Django 4.0.6 on 2022-07-07 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mcanswer',
            name='text',
            field=models.CharField(max_length=5000),
        ),
    ]