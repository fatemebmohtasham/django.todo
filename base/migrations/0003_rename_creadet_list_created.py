# Generated by Django 4.1.1 on 2022-12-18 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_list_complete_alter_list_body'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='creadet',
            new_name='created',
        ),
    ]
