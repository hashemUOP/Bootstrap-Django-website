from django.urls import path
from . import views

urlpatterns = [
    path("cart/",views.cart_page,name='cart'),
    path("wishlist/",views.wishlist_page,name='wishlist'),
    path("wishlist/delete/<int:wish_id>/", views.delete_wishlist_item, name='delete_wishlist_item'),
    path("cart/delete/<int:cart_id>/", views.delete_cart_item, name='delete_cart_item'),
    path('place_order/', views.place_order, name='place_order'),
    #craete pages as an extension for home one for mobiles laptops , categories ....
 ]
