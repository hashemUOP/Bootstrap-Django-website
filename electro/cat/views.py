from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import ProductModel  # Do not change this code as so the program will be destroyed
from shopping.models import Wishlist, Cart  # Do not change this code as so the program will be destroyed


def cat(request):
    return render(request, "catgories.html")


def lap(request):
    user = request.user
    total_price = 0
    num_of_items = 0
    num_of_wishlist_items = 0
    products_instances = ProductModel.objects.filter(cat="Laptops")

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
    return render(request,"laptop.html" , {
        'user': user,
        'cart_items': all_user_cart_items,
        'total': total_price,
        'num_of_items': num_of_items,
        'num_of_wishlist_items': num_of_wishlist_items,
        "products_instances": products_instances
    })


def access(request):
    user = request.user
    total_price = 0
    num_of_items = 0
    num_of_wishlist_items = 0
    products_instances = ProductModel.objects.filter(cat="Accessories")
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
    return render(request, "accessories.html", {
        'user': user,
        'cart_items': all_user_cart_items,
        'total': total_price,
        'num_of_items': num_of_items,
        'num_of_wishlist_items': num_of_wishlist_items,
        "products_instances": products_instances
    })



@login_required
def add_to_wishlist(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        if not product_id:
            return redirect('home')  # Redirect if product_id is missing

        product = get_object_or_404(ProductModel, ID=product_id)
        Wishlist.objects.get_or_create(
            user=request.user,
            product_id=product.ID,
            defaults={
                'product_name': product.name,
                'price': product.price,
                'image1': product.image1,
            }
        )
        return redirect('wishlist')

    return redirect('home')


@login_required
def add_to_cart(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        if not product_id:
            return redirect('home')  # Redirect if product_id is missing

        product = get_object_or_404(ProductModel, ID=product_id)
        cart_item, created = Cart.objects.get_or_create(
            user=request.user,
            product_id=product.ID,
            defaults={
                'product_name': product.name,
                'price': product.price,
                'image1': product.image1,
                'desc': product.desc if hasattr(product, 'desc') else "",
                'quantity': 1  # Default to 1 if not provided
            }
        )
        if not created:
            cart_item.quantity += 1
            cart_item.save()

        return redirect('cart')

    return redirect('home')


def camera(request):
    user = request.user
    total_price = 0
    num_of_items = 0
    num_of_wishlist_items = 0
    products_instances = ProductModel.objects.filter(cat="Cameras")
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
    return render(request, "camera.html", {
        'user': user,
        'cart_items': all_user_cart_items,
        'total': total_price,
        'num_of_items': num_of_items,
        'num_of_wishlist_items': num_of_wishlist_items,
        "products_instances": products_instances
    })


def phones(request):
    products_instances = ProductModel.objects.filter(cat="SmartPhones")
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
    return render(request, "phones.html", {
        'user': user,
        'cart_items': all_user_cart_items,
        'total': total_price,
        'num_of_items': num_of_items,
        'num_of_wishlist_items': num_of_wishlist_items,
        "products_instances": products_instances
    })


def headphones(request):
    products_instances = ProductModel.objects.filter(cat="HeadSets")
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
    return render(request, "headphones.html", {
        'user': user,
        'cart_items': all_user_cart_items,
        'total': total_price,
        'num_of_items': num_of_items,
        'num_of_wishlist_items': num_of_wishlist_items,
        "products_instances": products_instances
    })
