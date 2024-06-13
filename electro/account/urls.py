from django.urls import path
from .views import create_account, ProfileView, AccountLogin, AccountLogout

urlpatterns = [
    path('create/', create_account, name='create_account'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', AccountLogin.as_view(), name='login'),
    path('logout/', AccountLogout.as_view(), name='logout'),
]
