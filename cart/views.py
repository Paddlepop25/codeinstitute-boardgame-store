from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from catalogue.models import Game

def view_cart(request):
    # retrieve the cart
    cart = request.session.get('shopping_cart', {})
    
    return render(request, 'cart/view_cart.template.html', {
        'shopping_cart':cart
    })
    
def add_to_cart(request, game_id):
    # attempt to get existing cart from the session using the key "shopping_cart"
    # the second argument will be the default value if 
    # if the key does not exist in the session
    cart = request.session.get('shopping_cart', {})
    
    # we check if the game_id is not in the cart. If so, we will add it
    if game_id not in cart:
        game = get_object_or_404(Game, pk=game_id)
        # game is found, let's add it to the cart
        cart[game_id] = {
            'id':game_id,
            'name': game.name,
            'price': str(game.price),
            'image_url':game.image.cdn_url,
            'quantity':1,
            }
        
        # save the cart back to sessions
        request.session['shopping_cart'] = cart
        messages.success(request, "Game has been added to your cart!")
        return redirect('/cart/')
        # return render(request, 'catalogue/games.template.html')  
        
    else:
        cart[game_id]['quantity']+=1
        request.session['shopping_cart'] = cart
        total_price = round(int(cart[game_id]['quantity']) * float(cart[game_id]['price']),2)
        return render(request, 'cart/view_cart.template.html', {
            'total_price':total_price
        })
        
def minus_from_cart(request, game_id):
    print("Hi")
    cart = request.session.get('shopping_cart', {})
    
    if game_id not in cart:
        game = get_object_or_404(Game, pk=game_id)
        cart[game_id] = {
            'id':game_id,
            'name': game.name,
            'price': str(game.price),
            'image_url':game.image.cdn_url,
            'quantity':1,
            }
        
        # save the cart back to sessions
        request.session['shopping_cart'] = cart
        messages.success(request, "Game has been removed from your cart")
        return redirect('/cart/')
        
    else:
        cart[game_id]['quantity']-=1
        request.session['shopping_cart'] = cart
        total_price = round(int(cart[game_id]['quantity']) * float(cart[game_id]['price']),2)
        return render(request, 'cart/view_cart.template.html', {
            'total_price':total_price
        })        
        
def grand_total_price(request, game_id):
    cart = request.session.get('shopping_cart')
    print("hi")
    request.session['shopping_cart'] = cart
    total_price = len(cart.total_price)
    
    grand_total_price = 0
    if total_price > 0:
        for price in total_price:
            grand_total_price += price
    # print(int(cart[game_id]['quantity']))
    return render(request, 'cart/view_cart.template.html', {
    'grand_total_price':grand_total_price
    })
    
def remove_from_cart(request, game_id):
    # retrieve the cart from session
    cart = request.session.get('shopping_cart',{})
    
    # if the game is in the cart
    if game_id in cart:
        # remove it from the cart
        del cart[game_id]
        # save back to the session
        request.session['shopping_cart'] = cart
        messages.success(request, "Item removed from cart successfully!")
        
    # return redirect('/catalogue/')    
        return render(request, 'cart/view_cart.template.html')

@login_required        
def checkout_form(request):
    return render(request, 'cart/checkout_form.template.html')        
    
    