# Generated by Django 4.1.5 on 2023-11-11 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alternatif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_alternatif', models.CharField(max_length=50, unique=True)),
                ('simbol', models.CharField(max_length=5, unique=True)),
                ('nim', models.CharField(max_length=12, unique=True)),
                ('alamat', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Gap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nilai', models.IntegerField()),
                ('gap', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Kriteria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_kriteria', models.CharField(max_length=50, unique=True)),
                ('nilai_target', models.IntegerField()),
            ],
        ),
    ]
