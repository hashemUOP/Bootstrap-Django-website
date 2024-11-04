from django.shortcuts import render, get_object_or_404, redirect
from shopping.models import Cart, Wishlist  # Keep this as required


def home_page(request):
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
    return render(request, "home.html", {
        'user': user,
        'cart_items': all_user_cart_items,
        'total': total_price,
        'num_of_items': num_of_items,
        'num_of_wishlist_items': num_of_wishlist_items
    })


def remove_cart_item(request, cart_id):
    cart_item = get_object_or_404(Cart, cart_id=cart_id)
    cart_item.delete()
    return redirect('home')
