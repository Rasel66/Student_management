# Generated by Django 5.0.6 on 2024-06-09 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('field_of_study', models.CharField(max_length=100)),
                ('result', models.FloatField()),
            ],
        ),
    ]
