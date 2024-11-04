from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import ProductModel
from shopping.models import Wishlist,Cart


def ProductViews(request, product_id):
    uop_instance = ProductModel.objects.get(pk = product_id)
    user = request.user
    total_price = 0
    num_of_items = 0
    num_of_wishlist_items = 0

    # Check if the user is authenticated before accessing user-specific items
    if user.is_authenticated:
        all_user_cart_items = Cart.objects.filter(user=user)
        num_of_items = all_user_cart_items.count()

        # Calculate total price for authenticated user's cart items
        for item in all_user_cart_items:
            total_price += item.price * item.quantity

        # Count wishlist items
        all_user_wishlist_items = Wishlist.objects.filter(user=user)
        num_of_wishlist_items = all_user_wishlist_items.count()
    else:
        # If user is not authenticated, provide default values
        all_user_cart_items = []
        num_of_items = 0
        total_price = 0
        num_of_wishlist_items = 0

    # Render the template with the context
    if uop_instance is not None:
        return render(request, "product.html", {
        'user': user,
        'cart_items': all_user_cart_items,
        'total': total_price,
        'num_of_items': num_of_items,
        'num_of_wishlist_items': num_of_wishlist_items,
        "uop_instance": uop_instance
    })
    else:
        raise Http404('product doesnt exist')



