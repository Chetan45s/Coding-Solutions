# Generated by Django 3.0.5 on 2020-05-17 17:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='study_guide',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]