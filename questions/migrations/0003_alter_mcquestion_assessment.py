# Generated by Django 4.0.6 on 2022-07-07 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0002_initial'),
        ('questions', '0002_alter_mcanswer_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mcquestion',
            name='assessment',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='assessment.assessment'),
        ),
    ]