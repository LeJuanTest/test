# Generated by Django 5.0.1 on 2024-01-12 05:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='follower_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.profile'),
        ),
    ]