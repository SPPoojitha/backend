# Generated by Django 4.1.13 on 2024-01-29 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_blog_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to='blogs'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='blogs'),
        ),
    ]