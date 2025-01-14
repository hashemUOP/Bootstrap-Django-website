from django.core.paginator import Paginator
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
    page_obj = product_list(request,"Laptops")

    # check if  user is authenticated before accessing user specific items
    if user.is_authenticated:
        all_user_cart_items = Cart.objects.filter(user=user)
        num_of_items = all_user_cart_items.count()

        # calculate total price for authenticated users cart items
        for item in all_user_cart_items:
            total_price += item.price * item.quantity

        # Count wishlist items
        all_user_wishlist_items = Wishlist.objects.filter(user=user)
        num_of_wishlist_items = all_user_wishlist_items.count()
    else:
        # if user is not authenticated set default values
        all_user_cart_items = []
        num_of_items = 0
        total_price = 0
        num_of_wishlist_items = 0

    return render(request, "laptop.html", {
        'user': user,
        'cart_items': all_user_cart_items,
        'total': total_price,
        'num_of_items': num_of_items,
        'num_of_wishlist_items': num_of_wishlist_items,
        "products_instances": products_instances,
        'page_obj': page_obj,
    })


def access(request):
    user = request.user
    total_price = 0
    num_of_items = 0
    num_of_wishlist_items = 0
    products_instances = ProductModel.objects.filter(cat="Accessories")
    if user.is_authenticated:
        all_user_cart_items = Cart.objects.filter(user=user)
        num_of_items = all_user_cart_items.count()

        for item in all_user_cart_items:
            total_price += item.price * item.quantity

        # count wishlist items
        all_user_wishlist_items = Wishlist.objects.filter(user=user)
        num_of_wishlist_items = all_user_wishlist_items.count()
    else:
        all_user_cart_items = []
        num_of_items = 0
        total_price = 0
        num_of_wishlist_items = 0

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
            return redirect('home')  # redirect if product_id is missing

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
            return redirect('home')  # redirect if product_id is missing

        product = get_object_or_404(ProductModel, ID=product_id)
        cart_item, created = Cart.objects.get_or_create(
            user=request.user,
            product_id=product.ID,
            defaults={
                'product_name': product.name,
                'price': product.price,
                'image1': product.image1,
                'desc': product.desc if hasattr(product, 'desc') else "",
                'quantity': 1  # default to 1 if not provided
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
    if user.is_authenticated:
        all_user_cart_items = Cart.objects.filter(user=user)
        num_of_items = all_user_cart_items.count()

        for item in all_user_cart_items:
            total_price += item.price * item.quantity

        # count wishlist items
        all_user_wishlist_items = Wishlist.objects.filter(user=user)
        num_of_wishlist_items = all_user_wishlist_items.count()
    else:
        # if user is not authenticate set default values
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

    # check if the user is authenticated before accessing user specific items
    if user.is_authenticated:
        all_user_cart_items = Cart.objects.filter(user=user)
        num_of_items = all_user_cart_items.count()

        # calculate total price for authenticated users cart items
        for item in all_user_cart_items:
            total_price += item.price * item.quantity

        # count wishlist items
        all_user_wishlist_items = Wishlist.objects.filter(user=user)
        num_of_wishlist_items = all_user_wishlist_items.count()
    else:
        # if user is not authenticated set default values
        all_user_cart_items = []
        num_of_items = 0
        total_price = 0
        num_of_wishlist_items = 0

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

    # check if the user is authenticated before accessing user specific items
    if user.is_authenticated:
        all_user_cart_items = Cart.objects.filter(user=user)
        num_of_items = all_user_cart_items.count()

        # calculate total price for authenticated users cart items
        for item in all_user_cart_items:
            total_price += item.price * item.quantity

        # count wishlist items
        all_user_wishlist_items = Wishlist.objects.filter(user=user)
        num_of_wishlist_items = all_user_wishlist_items.count()
    else:
        # if user is not authenticated set default values
        all_user_cart_items = []
        num_of_items = 0
        total_price = 0
        num_of_wishlist_items = 0

    return render(request, "headphones.html", {
        'user': user,
        'cart_items': all_user_cart_items,
        'total': total_price,
        'num_of_items': num_of_items,
        'num_of_wishlist_items': num_of_wishlist_items,
        "products_instances": products_instances
    })


def product_list(request, category):

    products = ProductModel.objects.filter(cat=category)  # fetch products in the specified category
    paginator = Paginator(products, 6)  # paginate with 6 products per page

    page_number = request.GET.get('page')  # retrieve page number from query string
    page_obj = paginator.get_page(page_number)  # get the products for the current page

    return page_obj