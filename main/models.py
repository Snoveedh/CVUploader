from django.db import models



STATE_CHOICE = (
('AndhraPradesh','AndhraPradesh'),
('Assam','Assam'),
('Bihar','Bihar'),
('Chhattisgarh','Chhattisgarh'),
('Goa','Goa'),
('Gujarat','Gujarat'),
('Haryana','Haryana'),
('HimachalPradesh','HimachalPradesh'),
('JammuandKashmir','JammuandKashmir'),
('Jharkhand','Jharkhand'),
('Karnataka','Karnataka'),
('Kerala','Kerala'),
('MadhyaPradesh','MadhyaPradesh'),
('Maharashtra','Maharashtra'),
('Manipur','Manipur'),
('Meghalaya','Meghalaya'),
('Mizoram','Mizoram'),
('Nagaland','Nagaland'),
('Odisha','Odisha'),
('Punjab','Punjab'),
('Rajasthan','Rajasthan'),
('Sikkim','Sikkim'),
('TamilNadu','TamilNadu'),
('Telangana','Telangana'),
('Tripura','Tripura'),
('UttarPradesh','UttarPradesh'),
('Uttarakhand','Uttarakhand'),
('WestBengal','WestBengal'),
('AndamanandNicobarIslands','AndamanandNicobarIslands'),
('Chandigarh','Chandigarh'),
('DadraandNagarHaveli','DadraandNagarHaveli'),
('DamanandDiu','DamanandDiu'),
('Lakshadweep','Lakshadweep'),
('NationalCapitalTerritoryofDelhi','NationalCapitalTerritoryofDelhi'),
('Puducherry','Puducherry'),
('ArunachalPradesh','ArunachalPradesh'),
)


class Resume(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.PositiveIntegerField()
    state = models.CharField(choices= STATE_CHOICE, max_length=50)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='profileimg', blank=True)
    my_file = models.FileField(upload_to='doc',blank=True)