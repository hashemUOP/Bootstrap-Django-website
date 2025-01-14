from django.shortcuts import get_object_or_404, render, redirect
from .models import Wishlist, Cart, Order  # Keep these imports as required


def wishlist_page(request):
    # Check if user is authenticated, filter wishlist items accordingly
    user = request.user
    num_of_wishlist_items = 0
    num_of_items = 0
    total_price = 0
    if user.is_authenticated:
        all_user_cart_items = Cart.objects.filter(user=user)  # Filter for the logged-in user’s items
        for item in all_user_cart_items:
            num_of_items = num_of_items + 1
            total_price += item.price * item.quantity
    else:
        all_user_cart_items = []

    net_total = total_price + 10  # Add fixed handling charge to total price

    if user.is_authenticated:
        all_user_wishlist_items = Wishlist.objects.filter(user=user)
        num_of_wishlist_items = all_user_wishlist_items.count()
    else:
        all_user_wishlist_items = []

    return render(request, "wishlist.html", {
        'user': user,
        'wishlist_items': all_user_wishlist_items,
        'cart_items': all_user_cart_items,
        'total': total_price,
        'net_total': net_total,
        'num_of_items': num_of_items,
        'num_of_wishlist_items': num_of_wishlist_items
    })


def delete_cart_item(request, cart_id):
    if request.user.is_authenticated:
        cart_item = get_object_or_404(Cart, cart_id=cart_id, user=request.user)  # Filter by authenticated user
        cart_item.delete()
    return redirect('cart')  # Redirect back to the cart page


def cart_page(request):
    user = request.user
    total_price = 0
    num_of_wishlist_items = 0
    num_of_items = 0
    if user.is_authenticated:
        all_user_cart_items = Cart.objects.filter(user=user)  # Filter for the logged-in user’s items
        for item in all_user_cart_items:
            num_of_items = num_of_items + 1
            total_price += item.price * item.quantity
    else:
        all_user_cart_items = []

    net_total = total_price + 10  # Add fixed handling charge to total price
    all_user_wishlist_items = Wishlist.objects.filter(user=user)
    num_of_wishlist_items = all_user_wishlist_items.count()
    return render(request, "cart.html", {
        'user': user,
        'cart_items': all_user_cart_items,
        'total': total_price,
        'net_total': net_total,
        'num_of_items': num_of_items,
        'num_of_wishlist_items': num_of_wishlist_items
    })


def delete_wishlist_item(request, wish_id):
    if request.user.is_authenticated:
        wishlist_item = get_object_or_404(Wishlist, wish_id=wish_id, user=request.user)  # Filter by authenticated user
        wishlist_item.delete()
    return redirect('wishlist')  # Redirect back to the wishlist page


def place_order(request):
    if request.method == 'POST':
        # Ensure the user is authenticated before placing an order
        if not request.user.is_authenticated:
            return redirect('login')  # Redirect to login if user is not authenticated

        # Retrieve form data
        user = request.user
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        notes = request.POST.get('notes')

        # Calculate total price for the user's cart items
        total_price = 0
        user_cart_items = Cart.objects.filter(user=user)
        for item in user_cart_items:
            total_price += item.price * item.quantity

        net_total = total_price + 10  # Include any additional charges

        # Create and save the Order
        order = Order(
            user=user,
            address=address,
            city=city,
            state=state,
            zip_code=zipcode,
            name=name,
            email=email,
            phone_num=phone,
            notes=notes,
            net_total=net_total
        )
        order.save()

        # Clear the cart after placing the order
        user_cart_items.delete()

        return redirect('home')  # Redirect to home on successful order

    return render(request, 'cart.html')  # Render the cart page if accessed via GET
