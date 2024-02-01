# Generated by Django 4.2 on 2023-08-31 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_booktable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booktable',
            name='datetime',
        ),
        migrations.RemoveField(
            model_name='booktable',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='booktable',
            name='time',
        ),
        migrations.AlterField(
            model_name='booktable',
            name='persons',
            field=models.CharField(choices=[('1', 'Number of guests 1'), ('2', 'Number of guests 2'), ('3', 'Number of guests 3'), ('4', 'Number of guests 4'), ('5', 'Number of guests 5')], max_length=50),
        ),
    ]