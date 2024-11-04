from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .forms import LoginForm, CreateAccountForm
from .models import UserProfile


# Profile view that requires login to access
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # Ensure a UserProfile exists for the logged-in user
        profile, created = UserProfile.objects.get_or_create(user=user)
        context['user'] = user
        context['profile'] = profile
        return context


# Custom login view that renders a login form and redirects to the profile page
class AccountLogin(LoginView):
    template_name = "login.html"
    next_page = reverse_lazy("profile")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = LoginForm()
        return context


# Custom logout view with redirection to the home page
class AccountLogout(LogoutView):
    http_method_names = ["get", "post"]
    next_page = reverse_lazy("home")


# View for creating a new account and associated UserProfile
def create_account(request):
    if request.method == 'POST':
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            # Create the user with form data
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1'],
            )
            # Create a UserProfile for the user with additional details
            UserProfile.objects.create(
                user=user,
                address=form.cleaned_data['address'],
                phone_number=form.cleaned_data['phone_number']
            )
            return redirect('login')  # Redirect to login after successful account creation
    else:
        form = CreateAccountForm()  # Display an empty form if request method is not POST

    return render(request, 'create.html', {'form': form})  # Render the create account page
