# Generated by Django 3.0.5 on 2022-12-08 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topping',
            old_name='name',
            new_name='topping_name',
        ),
    ]
