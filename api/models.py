from django.db import models

# Create your models here.

class Vendor (models.Model):
    name= models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

    def natural_key(self):
        return self.name

    
class Market (models.Model):
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
    name=models.CharField(max_length=200)
    vendor= models.ForeignKey(Vendor,on_delete=models.CASCADE)
    address= models.CharField(max_length=1000,blank=True)
    day_open= models.CharField(max_length=2,choices=DAYS_OF_THE_WEEK,null=True)
    day_close= models.CharField(max_length=2,choices=DAYS_OF_THE_WEEK,null=True)
    time_open= models.TimeField(null=True)
    time_close=models.TimeField(null=True)

    def __str__(self):
        return self.name

    def natural_key(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(max_length=1000,blank=True)

    def __str__(self):
        return self.name

    def natural_key(self):
        return self.name

    
class Item(models.Model):
    market= models.ForeignKey(Market,on_delete=models.CASCADE)
    product= models.ForeignKey(Product,on_delete=models.CASCADE)
    price= models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return '%s, %s' % (self.product,self.market)

    class Meta:
        constraints=[
            models.UniqueConstraint(fields=['market','product'],name='unique_product_per_market')
        ]