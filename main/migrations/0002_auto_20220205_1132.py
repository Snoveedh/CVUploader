# Generated by Django 3.2.9 on 2022-02-05 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='my_file',
            field=models.FileField(upload_to='doc'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='profile_image',
            field=models.ImageField(upload_to='profile_img'),
        ),
    ]