# Generated by Django 4.1.5 on 2023-11-11 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gap',
            name='gap',
            field=models.FloatField(),
        ),
    ]
