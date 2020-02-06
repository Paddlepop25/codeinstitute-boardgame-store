from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from catalogue.models import Game

def add_to_cart(request, game_id):
    # attempt to get existing cart from the session using the key "shopping_cart"
    # the second argument will be the default value if 
    # if the key does not exist in the session
    cart = request.session.get('shopping_cart', {})
    
    # we check if the course_id is not in the cart. If so, we will add it
    if game_id not in cart:
        game = get_object_or_404(Game, pk=game_id)
        # game is found, let's add it to the cart
        cart[game_id] = {
            'id':game_id,
            'name': game.name,
            'price': str(game.price),
            'image_url':game.image.cdn_url
            }
        
        # save the cart back to sessions
        request.session['shopping_cart'] = cart
        messages.success(request, "Game has been added to your cart!")
        return redirect('/catalogue/')
    else:
        return redirect('/catalogue/')

def view_cart(request):
    # retrieve the cart
    cart = request.session.get('shopping_cart', {})
    
    return render(request, 'cart/view_cart.template.html', {
        'shopping_cart':cart
    })
    
def remove_from_cart(request, game_id):
    # retrieve the cart from session
    cart = request.session.get('shopping_cart',{})
    
    # if the course is in the cart
    if game_id in cart:
        # remove it from the cart
        del cart[game_id]
        # save back to the session
        request.session['shopping_cart'] = cart
        messages.success(request, "Item removed from cart successfully!")
        
    # return redirect('/catalogue/')    
        return render(request, 'cart/view_cart.template.html')
        
def checkout_form(request):
    return render(request, 'cart/checkout_form.template.html')        
    
    