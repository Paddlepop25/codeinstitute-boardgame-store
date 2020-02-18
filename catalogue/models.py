from django.db import models
# from django.core.validators import MinValueValidator, MaxValueValidator
from pyuploadcare.dj.models import ImageField

# Create your models here.
class Game(models.Model):
    name = models.CharField(blank=False, max_length=21)
    description = models.TextField(blank=False)
    inside_box = models.TextField(blank=True)
    # available = models.BooleanField(blank=True)
    # stock_left = models.IntegerField(default=0, blank=True, validators=[MinValueValidator(0), MaxValueValidator(99)])
    # stock_left = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    price = models.DecimalField(default=0, max_digits=5, decimal_places=2, blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = ImageField(null=True, blank=True)
    
    def __str__(self):
        # return "{} x {} ({})".format(self.name, self.stock_left, self.category)
        return "{} ({})".format(self.name, self.category)
        
class Category(models.Model):
    name = models.CharField(max_length=50, blank=False)
    
    def __str__(self):
        # return "{} (id: {})".format(self.name, self.id)
        return self.name