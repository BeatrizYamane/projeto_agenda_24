# Generated by Django 5.0.7 on 2024-07-22 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='create_date',
            new_name='created_date',
        ),
        migrations.AddField(
            model_name='contact',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]