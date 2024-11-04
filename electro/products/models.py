from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class ProductModel(models.Model):
    ID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    desc = models.CharField(max_length=500)
    details = models.CharField(max_length=500)
    cat = models.CharField(max_length=50, default='Category')
    image1 = models.ImageField(upload_to='technest/images/products')
    image2 = models.ImageField(upload_to='technest/images/products')
    image3 = models.ImageField(upload_to='technest/images/products')
    image4 = models.ImageField(upload_to='technest/images/products')

    def __str__(self):
        return str(self.ID)

class UserReview():
    review_id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    star_reviews = models.IntegerField()
    email = models.EmailField()
    review = models.TextField()
    def __str__(self):
        return f'{self.user} wishlist {self.product_name}'
