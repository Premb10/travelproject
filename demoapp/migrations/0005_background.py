# Generated by Django 4.2.1 on 2023-06-03 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0004_delete_background'),
    ]

    operations = [
        migrations.CreateModel(
            name='background',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='bg_image')),
            ],
        ),
    ]
