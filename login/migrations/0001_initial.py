# Generated by Django 5.1.3 on 2024-11-30 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('phonenumber', models.CharField(max_length=11, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]
