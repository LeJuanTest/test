# Generated by Django 5.0.1 on 2024-03-18 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_comment_image_comment_comment_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_profile',
            new_name='comments_profile',
        ),
    ]
