# Generated by Django 4.1.13 on 2024-02-04 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_remove_comment_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
