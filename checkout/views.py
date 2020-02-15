from django.shortcuts import render, reverse, HttpResponse, get_object_or_404
from .forms import OrderForm, PaymentForm


#import settings so that we can access the public stripe key
from django.conf import settings
# import stripe

# from catalogue.models import Game

# Create your views here.

def donate(request):
    return render(request, 'checkout/donate.template.html')

def charge(request):
    order_form = OrderForm()
    payment_form = PaymentForm()
    amount = request.GET['amount']
    # if request.method == 'GET':
        #show form
    return render(request, 'checkout/charge.html', {
        # 'publishable' : settings.STRIPE_PUBLISHABLE_KEY,
        'order_form' : OrderForm,
        'payment_form' : PaymentForm,
        'amount': amount
    })
    
# simple method
# def checkout(request):
#     stripe.api_key = settings.STRIPE_SECRET_KEY
    
#     # retrieve shopping cart
#     cart = request.session.get('shopping_cart', {})
    
#     line_items = []
    
#     # generate the line_items
#     for id,game in cart.items():
#         # For each item in the cart, get its details from the database
#         game_from_db = get_object_or_404(Game, pk=id)
#         line_items.append({
#             'name': game_from_db.name,
#             'amount': int(game_from_db.price*100), #convert to cents, in integer
#             'currency':'sgd',
#             'quantity':game['quantity']
#         })
    
#     #generate the session
#     session = stripe.checkout.Session.create(
#         payment_method_types=['card'],
#         line_items=line_items,
#         success_url=request.build_absolute_uri(reverse(checkout_success)),
#         cancel_url=request.build_absolute_uri(reverse(checkout_cancelled)),
#         payment_intent_data={
#             'capture_method':'manual'
#         }
#     )
    
#     # render the template
#     return render(request, 'checkout/checkout.template.html', {
#         'session_id':session.id,
#         'public_key': settings.STRIPE_PUBLISHABLE_KEY
#     })
    
# def checkout_success(request):
#     request.session['shopping_cart'] = {}
#     return render(request, 'checkout/checkout_success.template.html')
    
# def checkout_cancelled(request):
#     return HttpResponse("Checkout cancelled")
    
    
    