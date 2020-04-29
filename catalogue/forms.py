from django import forms
from .models import Game
from pyuploadcare.dj.forms import ImageField, FileWidget

class GameForm(forms.ModelForm):
    price = forms.DecimalField(min_value=1, max_digits=5, decimal_places=2)
    # homepage_display is used as filtered field to display on homepage
    homepage_display = forms.BooleanField(required=False)

    class Meta:
        image = ImageField(widget=FileWidget(attrs={'data-clearable':True}))
        model=Game
        # fields will display on form as arranged
        fields=('name', 'category', 'description', 'inside_box', 'price', 'image', 'homepage_display')

class GameSearchForm(forms.Form):
    search_terms = forms.CharField(required=False)