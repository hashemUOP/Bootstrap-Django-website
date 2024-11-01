from django.urls import path
from . import views

urlpatterns = [
    path('products/<int:product_id>/', views.ProductViews, name='product_detail'),
]
