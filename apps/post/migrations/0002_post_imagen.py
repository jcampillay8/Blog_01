# Generated by Django 3.1 on 2021-08-11 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagen',
            field=models.ImageField(default='imagen', upload_to='imagenes/'),
        ),
    ]