from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("",views.home_page,name='home'),
    path("cart/delete/<int:cart_id>/", views.remove_cart_item, name='remove_cart_item'),
    #craete pages as an extension for home one for mobiles laptops , categories ....
 ]