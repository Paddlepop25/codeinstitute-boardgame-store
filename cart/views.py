from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from catalogue.models import Game

def view_cart(request):
    # retrieve the cart, the second argument {} will be the default value if 
    # if the key does not exist in the session
    cart = request.session.get('shopping_cart', {})
    delivery = 0.00
    grand_total_price = 0.00
    for game_id,game in cart.items():
        grand_total_price += game['total_price']
        
    # $8 delivery charge applies for orders below $300    
    if grand_total_price <= 300:
        grand_total_price = grand_total_price + 8.00
        delivery = 8.00
    else: 
        grand_total_price = grand_total_price
        delivery = 0.00
        
    return render(request, 'cart/view_cart.template.html', {
        'shopping_cart':cart,
        'delivery':delivery,
        'grand_total_price':round(grand_total_price, 2)
    })
    
def add_to_cart(request, game_id):
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
            'total_price':float(game.price)
            }
        
        # save the cart back to sessions
        request.session['shopping_cart'] = cart
        messages.success(request, "Game has been added to your cart")
        return redirect('/catalogue/')
        
    else:
        cart[game_id]['quantity']+=1
        cart[game_id]['total_price'] = round(int(cart[game_id]['quantity']) * float(cart[game_id]['price']),2)
        request.session['shopping_cart'] = cart
        return redirect('/cart/')
        
def total_price(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    cart = request.session.get('shopping_cart', {})
    cart[game_id] = {
    'id':game_id,
    'name': game.name,
    'price': str(game.price),
    'image_url':game.image.cdn_url,
    'quantity':cart['quantity'],
    'total_price':round(int(cart[game_id]['quantity']) * float(cart[game_id]['price']),2)
    }
    request.session['shopping_cart'] = cart
    return render(request, 'cart/view_cart.template.html', {
            'total_price':total_price
        })        
     
def minus_from_cart(request, game_id):
    cart = request.session.get('shopping_cart', {})
    if game_id in cart:
        game = get_object_or_404(Game, pk=game_id) 
        if cart[game_id]['quantity'] > 1:
            cart[game_id]['quantity']-=1
            cart[game_id]['total_price'] = round(int(cart[game_id]['quantity']) * float(cart[game_id]['price']),2)
        # save the cart back to sessions
            request.session['shopping_cart'] = cart
        return redirect('/cart/')
    
def remove_from_cart(request, game_id):
    # retrieve the cart from session
    cart = request.session.get('shopping_cart',{})
    # if the game is in the cart
    if game_id in cart:
        # remove it from the cart
        del cart[game_id]
        # save back to the session
        request.session['shopping_cart'] = cart
        messages.success(request, "Game has been removed from your cart")
        return redirect('/cart/')
     
    
    