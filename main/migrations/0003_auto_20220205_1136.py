# Generated by Django 3.2.9 on 2022-02-05 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220205_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='my_file',
            field=models.FileField(blank=True, upload_to='doc'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='profile_img'),
        ),
    ]
