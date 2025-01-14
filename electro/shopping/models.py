from django.contrib.auth.models import User
from django.db import models


# Wishlist model
class Wishlist(models.Model):
    wish_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=100)
    price = models.FloatField()
    image1 = models.ImageField(upload_to='technest/images/products')
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} wishlist {self.product_name}'


# Cart model
class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=100)
    price = models.FloatField()
    image1 = models.ImageField(upload_to='technest/images/products')
    desc = models.CharField(max_length=500)
    added_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.product_name} in cart for {self.user}'


class Order(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=60)
    zip_code = models.CharField(max_length=20)
    name = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    phone_num = models.CharField(max_length=15, unique=True)
    notes = models.TextField(max_length=500)
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    net_total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order {self.order_id} by {self.user}'  # Use order_id for clarity

