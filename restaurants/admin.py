from django.contrib import admin
from restaurants.models import Restaurant, MenuItem

class RestaurantAdmin(admin.ModelAdmin):
    pass

admin.site.register(Restaurant, RestaurantAdmin)

class MenuItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(MenuItem, MenuItemAdmin)