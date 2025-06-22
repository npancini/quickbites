from django.shortcuts import render
from restaurants.models import Restaurant
from restaurants.models import MenuItem

def restaurant_index(request):
    restaurants = Restaurant.objects.all()
    context = {
        "restaurants": restaurants
    }
    return render(request, "restaurants/restaurant_index.html", context)

def restaurant_menu(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    menu = restaurant.menuitem_set.all()
    context = {
        "restaurant": restaurant,
        "menu": menu
    }
    return render(request, "restaurants/restaurant_menu.html", context)