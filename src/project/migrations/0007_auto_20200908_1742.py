# Generated by Django 3.0.7 on 2020-09-08 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_team_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]