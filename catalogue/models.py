from django.db import models
from pyuploadcare.dj.models import ImageField

# define the game model with specific fields
class Game(models.Model):
    name = models.CharField(blank=False, max_length=21)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    description = models.TextField(blank=False)
    inside_box = models.TextField(blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    image = ImageField(null=True, blank=False)
    homepage_display = models.BooleanField(default=False)
    
    # set this view in the admin panel, e.g. Warhammer (Board Games)
    def __str__(self):
        return "{} ({})".format(self.name, self.category)
        
class Category(models.Model):
    name = models.CharField(max_length=50, blank=False)
    
    def __str__(self):
        return self.name