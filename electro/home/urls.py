from django.urls import path
from . import views
urlpatterns = [
    path("",views.home_page,name='home'),
    #craete pages as an extension for home one for mobiles laptops , categories ....
 ]