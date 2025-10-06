from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm, CustomAuthenticationForm

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = CustomAuthenticationForm

class CustomLogoutView(LogoutView):
    template_name = 'accounts/logout.html'

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard:panel')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
