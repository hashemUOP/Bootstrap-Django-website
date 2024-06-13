from django.contrib import admin
from .models import ProductModel

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('ID',)  # Make the 'ID' field read-only
    list_display = ('ID', 'name', 'price', 'cat')  # Display these fields in the admin list view

admin.site.register(ProductModel, ProductAdmin)
