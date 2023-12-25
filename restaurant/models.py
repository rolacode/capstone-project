from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guest = models.SmallIntegerField(default=6)
    booking_date = models.DateField()
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.title
    

class MenuItem(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=6, db_index=True, decimal_places=2)
    featured = models.BooleanField(db_index=True, default=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    inventory = models.SmallIntegerField(default=1)

    def get_menuitem(self):
        f'{self.title} : {str(self.price)}'   