# Generated by Django 3.2.9 on 2022-02-03 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=100)),
                ('locality', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('pin', models.PositiveIntegerField()),
                ('state', models.CharField(choices=[('AndhraPradesh', 'AndhraPradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('HimachalPradesh', 'HimachalPradesh'), ('JammuandKashmir', 'JammuandKashmir'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('MadhyaPradesh', 'MadhyaPradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('TamilNadu', 'TamilNadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('UttarPradesh', 'UttarPradesh'), ('Uttarakhand', 'Uttarakhand'), ('WestBengal', 'WestBengal'), ('AndamanandNicobarIslands', 'AndamanandNicobarIslands'), ('Chandigarh', 'Chandigarh'), ('DadraandNagarHaveli', 'DadraandNagarHaveli'), ('DamanandDiu', 'DamanandDiu'), ('Lakshadweep', 'Lakshadweep'), ('NationalCapitalTerritoryofDelhi', 'NationalCapitalTerritoryofDelhi'), ('Puducherry', 'Puducherry'), ('ArunachalPradesh', 'ArunachalPradesh')], max_length=50)),
                ('mobile', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('job_city', models.CharField(max_length=50)),
                ('profile_image', models.ImageField(blank=True, upload_to='profile_img')),
                ('my_file', models.FileField(blank=True, upload_to='doc')),
            ],
        ),
    ]
