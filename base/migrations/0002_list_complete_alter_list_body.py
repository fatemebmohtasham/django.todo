# Generated by Django 4.1.1 on 2022-09-15 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='list',
            name='body',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]