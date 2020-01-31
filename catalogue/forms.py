from django import forms
from .models import Game
from pyuploadcare.dj.forms import ImageField, FileWidget

class GameForm(forms.ModelForm):
    class Meta:
        image = ImageField(widget=FileWidget(attrs={'data-clearable':True}))
        model=Game
        fields=('name', 'description', 'inside_box', 'available', 'stock_left', 'price', 'category', 'image')