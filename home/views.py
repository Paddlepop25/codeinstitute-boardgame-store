from django.shortcuts import render
from catalogue.models import Game

def home(request):
    # displays only 8 games even though more 'homepage_display' checkboxes are ticked
    homepage_display = Game.objects.filter(homepage_display=True)[:8]
        
    return render(request, 'home/index.template.html', {
        'homepage_display':homepage_display
    })
