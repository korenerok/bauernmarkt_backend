from django.db import models

# Create your models here.

class Vendor (models.Model):
    name= models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    def natural_key(self):
        return self.name

    
class MarketEvent (models.Model):
    MONDAY = 'MO'
    TUESDAY = 'TU'
    WEDNESDAY = 'WE'
    THURSDAY = 'TH'
    FRIDAY = 'FR'
    SATURDAY = 'SA'
    SUNDAY  = 'SU'
    DAYS_OF_THE_WEEK=[
        (MONDAY,'Lunes'),
        (TUESDAY,'Martes'),
        (WEDNESDAY,'Miércoles'),
        (THURSDAY,'Jueves'),
        (FRIDAY,'Viernes'),
        (SATURDAY,'Sábado'),
        (SUNDAY,'Domingo')
    ]
    vendor= models.ForeignKey(Vendor,on_delete=models.CASCADE)
    address= models.CharField(max_length=500)
    day_open= models.CharField(max_length=2,choices=DAYS_OF_THE_WEEK)
    day_close= models.CharField(max_length=2,choices=DAYS_OF_THE_WEEK)
    time_open= models.TimeField()
    time_close=models.TimeField()
