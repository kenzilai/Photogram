# Generated by Django 4.1.7 on 2023-03-24 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='/media/avatars/default_profile.png', upload_to='media/avatars/'),
        ),
    ]
