# Generated by Django 3.0.8 on 2021-09-21 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0004_auto_20210921_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='titulo',
        ),
    ]
