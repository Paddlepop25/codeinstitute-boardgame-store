from django import forms
from .models import Game
from pyuploadcare.dj.forms import ImageField, FileWidget

class GameForm(forms.ModelForm):
    class Meta:
        image = ImageField(widget=FileWidget(attrs={'data-clearable':True}))
        model=Game
        fields=('name', 'description', 'inside_box', 'available', 'stock_left', 'price', 'category', 'image')
        
class GameSearchForm(forms.Form):
    search_terms = forms.CharField(required=False)
    # min_cost = forms.FloatField(required=False, min_value=0)
    # max_cost = forms.FloatField(required=False)      