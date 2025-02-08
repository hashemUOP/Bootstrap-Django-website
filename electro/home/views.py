from django.shortcuts import render, get_object_or_404, redirect
from shopping.models import Cart, Wishlist
from .recommendations import recommend_products


def home_page(request):
    user = request.user
    total_price = 0
    num_of_items = 0
    num_of_wishlist_items = 0
    # check if the user is authenticated first
    if user.is_authenticated:
        all_user_cart_items = Cart.objects.filter(user=user)
        num_of_items = all_user_cart_items.count()

        #  total price for authenticated user's cart items
        for item in all_user_cart_items:
            total_price += item.price * item.quantity

        # count wishlist items
        all_user_wishlist_items = Wishlist.objects.filter(user=user)
        num_of_wishlist_items = all_user_wishlist_items.count()
    else:
        # if user is not authenticated, provide default values
        all_user_cart_items = []
        num_of_items = 0
        total_price = 0
        num_of_wishlist_items = 0

    return render(request, "home.html", {
        'user': user,
        'cart_items': all_user_cart_items,
        'total': total_price,
        'num_of_items': num_of_items,
        'num_of_wishlist_items': num_of_wishlist_items,
        'products': recommend_view(request)
    })


def remove_cart_item(cart_id):
    cart_item = get_object_or_404(Cart, cart_id=cart_id)
    cart_item.delete()
    return redirect('home')



def recommend_view(request):
    user = request.user
    user_id = user.id
    if request.user.is_authenticated:
        user_id = request.user.id  # Get logged-in user ID
        recommended_products = recommend_products(user_id)  # Get recommended products
    else:
        recommended_products = []  # If user is not logged in, show no recommendations
    return recommended_products
