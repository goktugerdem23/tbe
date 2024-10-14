# Generated by Django 5.1.1 on 2024-09-30 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tbeapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
            ],
        ),
    ]
