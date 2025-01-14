from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.


from django.db import models


class ProductModel(models.Model):
    ID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    desc = models.CharField(max_length=500)
    details = models.CharField(max_length=500)
    cat = models.CharField(max_length=50, default='Category')
    image1 = models.URLField(max_length=500, blank=True, null=True)
    image2 = models.URLField(max_length=500, blank=True, null=True)
    image3 = models.URLField(max_length=500, blank=True, null=True)
    image4 = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return str(self.ID)


class UserReview(models.Model):
    review_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    star_reviews = models.IntegerField()
    email = models.EmailField()
    review = models.TextField()
    product_id = models.IntegerField()
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user} review {self.review_id} for product {self.product_id}'
