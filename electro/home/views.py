from django.shortcuts import render

# Create your views here.

def home_page(request):
    user = request.user
    return render(request , "home.html" ,{'user': user})