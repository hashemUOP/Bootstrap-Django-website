from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import ProductModel

def ProductViews(request, product_id):
    uop_instance = ProductModel.objects.get(pk = product_id)
    if uop_instance is not None:
        return render(request, 'product.html', {'uop_instance': uop_instance})
    else:
        raise Http404('product doesnt exist')



