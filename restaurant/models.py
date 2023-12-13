from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guest = models.SmallIntegerField(default=6)
    booking_date = models.DateField()
    
    def __str__(self):
        return self.name
    
    
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField(null=False)
    inventory = models.IntegerField(default=5)    
    
    def __str__(self):
        return self.title