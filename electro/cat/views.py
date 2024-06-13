from django.shortcuts import render


# Create your views here.

def cat(request):
    return render(request, "catgories.html")


def lap(request):
    return render(request, "laptop.html")


def access(request):
    return render(request, "accessories.html")


def camera(request):
    return render(request, "camera.html")


def phones(request):
    return render(request, "phones.html")


def headphones(request):
    return render(request,"headphones.html")