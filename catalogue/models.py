from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.
class Game(models.Model):
    # title = models.CharField(blank=False, max_length=255)
    # desc = models.TextField(blank=False)
    # number_of_hours = models.IntegerField(blank=False)
    # instructor = models.ForeignKey('Instructor', blank=True, null=True, on_delete=models.SET_NULL)
    
    name = models.CharField(blank=False, max_length=255)
    description = models.TextField(blank=False)
    inside_box = models.TextField(blank=False)
    available = models.BooleanField(blank=True)
    stock_left = models.IntegerField(default=0, blank=False)
    price = models.DecimalField(default=0, max_digits=5, decimal_places=2, blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    # discount = models.ManyToManyField('Discount')
    image = ImageField(null=True)
    
    def __str__(self):
        return "{} x {}".format(self.name, self.stock_left)
    
# class Instructor(models.Model):
#     first_name = models.CharField(blank=False, max_length=100)
#     last_name = models.CharField(blank=False, max_length=100)
    
#     def __str__(self):
#         return self.first_name + " " + self.last_name
        
class Category(models.Model):
    name = models.CharField(max_length=50, blank=False)
    
    def __str__(self):
        return "{} (id: {})".format(self.name, self.id)
        #return self.name + "( id:"+self.id+")"  
        
# class Discount(models.Model):
#     percent = models.IntegerField(blank=True)
    
#     def __str__(self):
#         return self.percent
  