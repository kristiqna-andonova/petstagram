# Generated by Django 5.1.1 on 2024-10-08 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_remove_like_to_photo_delete_comment_delete_like'),
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
