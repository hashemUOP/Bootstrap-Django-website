from django.urls import path
from . import views

urlpatterns = [
    path('products/<int:product_id>/', views.ProductViews, name='product_detail'),
    path('products/<int:product_id>/place_review/', views.place_review, name='place_review'),

]
