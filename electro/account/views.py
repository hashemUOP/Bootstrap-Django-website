from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .forms import LoginForm, CreateAccountForm
from .models import UserProfile


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        # Ensure a UserProfile exists for the user
        profile, created = UserProfile.objects.get_or_create(user=user)
        context['user'] = user
        context['profile'] = profile
        return context


class AccountLogin(LoginView):
    template_name = "login.html"
    next_page = reverse_lazy("profile")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = LoginForm()
        return context


class AccountLogout(LogoutView):
    http_method_names = ["get", "post"]
    next_page = reverse_lazy("home")

    def get(self, request):
        return super().post(request)


def create_account(request):
    if request.method == 'POST':
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1'],
            )
            # Create UserProfile instance
            profile = UserProfile.objects.create(
                user=user,
                address=form.cleaned_data['address'],
                phone_number=form.cleaned_data['phone_number']
            )
            return redirect('login')
    else:
        form = CreateAccountForm()
    return render(request, 'create.html', {'form': form})
