# Generated by Django 4.0.6 on 2022-07-05 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assessment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KataQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('all_tests_passed', models.BooleanField(default=False)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assessment.assessment')),
            ],
        ),
        migrations.CreateModel(
            name='SQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('marked_as_right', models.BooleanField(default=False)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assessment.assessment')),
            ],
            options={
                'verbose_name_plural': 'Subjective Questions',
            },
        ),
        migrations.CreateModel(
            name='MCQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assessment.assessment')),
            ],
            options={
                'verbose_name_plural': 'Multiple Choice Questions',
            },
        ),
        migrations.CreateModel(
            name='MCAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('correct', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.mcquestion')),
            ],
            options={
                'verbose_name_plural': 'Multiple Choice Answers',
            },
        ),
        migrations.CreateModel(
            name='KataTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(help_text='Create a test for your kata question', max_length=5000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.kataquestion')),
            ],
        ),
    ]
