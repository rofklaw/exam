from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from ..logreg.models import User
from .models import Item, Wishlist

def lander(request):
    data = {
    'my_wishes': Wishlist.objects.filter(User__id = request.session['id']),
    'all_wishes': Item.objects.all(),
    'my_id': request.session['id'],
    'my_name': request.session['first_name']
    }
    print data
    print data['my_wishes']
    print data['my_id']
    print data['my_name']
    return render(request, 'wishlist/lander.html', data)

def itemadder(request):
    return render(request, 'wishlist/itemadder.html')

def itemcreator(request):
    if len(request.POST['name']) < 3:
        messages.add_message(request, messages.ERROR, 'product must be at least 3 characters long')
        return redirect(reverse('itemadder'))
    user = User.objects.get(id = request.session['id'])
    try:
        wish = Item.objects.get(name = request.POST['name'])
        Wishlist.objects.create(User = user, Item = wish)
    except:
        wish = Item.objects.create(name = request.POST['name'], User = user)
        Wishlist.objects.create(User = user, Item = wish)

    return redirect(reverse('lander'))
# def inforoute(request):
#     id = Item

def iteminfo(request, id):
    info = {
    'theitem': Item.objects.get(id = id),
    'items': Item.objects.filter(id = id)
    }
    print info['items']
    return render(request, 'wishlist/iteminfo.html', info)

def deleteitem(request, id):
    Item.objects.get(id = id).delete()
    return redirect(reverse('lander'))

def takewish(request, id):
    Wishlist.objects.get(id = id).delete()
    return redirect(reverse('lander'))

def makewish(request, id):
    new_wish = Item.objects.get(id = id)
    user = User.objects.get(id = request.session['id'])
    Wishlist.objects.create(User = user, Item = new_wish)
    return redirect(reverse('lander'))

def logout(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect(reverse('home'))
