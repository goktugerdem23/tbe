# Generated by Django 5.1.1 on 2024-10-03 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tbeapp', '0005_seller'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seller',
            old_name='seller',
            new_name='seller_name',
        ),
    ]
