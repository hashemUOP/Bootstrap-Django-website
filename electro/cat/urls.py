from django.urls import path
from . import views

urlpatterns = [
    path("category/", views.cat, name='category'),
    path("category/laptops", views.lap, name='laptop'),
    path("category/accessories", views.access, name='access'),
    path("category/smartphones", views.phones, name='phones'),
    path("category/camera", views.camera, name='camera'),
    path("category/headphones",views.headphones,name = 'headphones'),
    path("wishlist/add/", views.add_to_wishlist, name='add_to_wishlist'),  # Add this line

]
