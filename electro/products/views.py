from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Sum
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import ProductModel, UserReview
from shopping.models import Wishlist, Cart
import math


def ProductViews(request, product_id):
    # Fetch product details
    uop_instance = ProductModel.objects.get(pk=product_id)
    product = get_object_or_404(ProductModel, ID=product_id)
    user = request.user

    total_num_of_stars = 0
    total_num_of_reviews = 0
    avg_stars = 0
    one_star_reviews = 0
    two_star_reviews = 0
    three_star_reviews = 0
    four_star_reviews = 0
    five_star_reviews = 0

    percentage_one_stars = 0
    percentage_two_stars = 0
    percentage_three_stars = 0
    percentage_four_stars = 0
    percentage_five_stars = 0



    if user.is_authenticated:
        total_num_of_reviews = UserReview.objects.filter(product_id=product_id).count()
        total_num_of_stars = UserReview.objects.filter(product_id=product_id).aggregate(Sum('star_reviews'))['star_reviews__sum'] or 0

        one_star_reviews = UserReview.objects.filter(product_id=product_id, star_reviews=1).count()
        two_star_reviews = UserReview.objects.filter(product_id=product_id, star_reviews=2).count()
        three_star_reviews = UserReview.objects.filter(product_id=product_id, star_reviews=3).count()
        four_star_reviews = UserReview.objects.filter(product_id=product_id, star_reviews=4).count()
        five_star_reviews = UserReview.objects.filter(product_id=product_id, star_reviews=5).count()

        percentage_one_stars = percentage(one_star_reviews,total_num_of_reviews)
        percentage_two_stars = percentage(two_star_reviews,total_num_of_reviews)
        percentage_three_stars = percentage(three_star_reviews,total_num_of_reviews)
        percentage_four_stars = percentage(four_star_reviews,total_num_of_reviews)
        percentage_five_stars = percentage(five_star_reviews,total_num_of_reviews)

        if total_num_of_reviews > 0:
            avg_stars = math.floor((total_num_of_stars / total_num_of_reviews) * 100) / 100
        else:
            avg_stars = 0
    # Fetch all reviews for the product
    reviews_list = UserReview.objects.filter(product_id=product_id).order_by('-create_date')

    # Handle pagination
    page = request.GET.get('page', 1)  # Get the current page number from the query string
    paginator = Paginator(reviews_list, 5)  # Paginate the reviews, 5 per page
    try:
        reviews = paginator.page(page)
    except PageNotAnInteger:
        # If page is invalid, default to the first page
        reviews = paginator.page(1)
    except EmptyPage:
        # If page is out of range, default to the last available page
        reviews = paginator.page(paginator.num_pages)

    # Render the template with the paginated reviews
    if uop_instance is not None:
        return render(request, "product.html", {
            'user': user,
            'cart_items': [],
            'total': 0,
            'num_of_items': 0,
            'num_of_wishlist_items': 0,
            'uop_instance': uop_instance,
            'product': product,
            'reviews': reviews,
            'star_range': range(1, 6),
            'avg_stars' : avg_stars,
            'num_of_stars' : total_num_of_stars,
            'num_of_reviews' : total_num_of_reviews,
            'one_star_reviews' : one_star_reviews,
            'two_star_reviews': two_star_reviews,
            'three_star_reviews': three_star_reviews,
            'four_star_reviews': four_star_reviews,
            'five_star_reviews': five_star_reviews,
            'percentage_one_stars' : percentage_one_stars,
            'percentage_two_stars': percentage_two_stars,
            'percentage_three_stars': percentage_three_stars,
            'percentage_four_stars': percentage_four_stars,
            'percentage_five_stars': percentage_five_stars,
        })
    else:
        raise Http404('Product does not exist')

def place_review(request, product_id):
    if request.method == 'POST':
        # ensure  user is authenticated before placing a review
        if not request.user.is_authenticated:
            return redirect('login')  # redirect to login if user is not authenticated

        # retrieve form data
        user = request.user
        star_reviews = request.POST.get('stars')
        email = request.POST.get('email')
        comment = request.POST.get('comment')

        # retrieve the product based on the provided product_id
        product = get_object_or_404(ProductModel, ID=product_id)

        # add review to db
        review = UserReview(
            user=user,
            email=email,
            review=comment,
            star_reviews=int(star_reviews),
            product_id=product.ID
        )
        review.save()


        return redirect('product_detail', product_id=product_id)

    return redirect('product_detail', product_id=product_id)    # redirect to product page if accessed via GET


def percentage(num_of_stars, total_reviews):
    if total_reviews == 0:
        return 0
    return (num_of_stars / total_reviews) * 100

