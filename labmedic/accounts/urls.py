from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CustomLoginView, CustomLogoutView, register
from .forms import CustomAuthenticationForm

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='accounts/login.html',
        authentication_form=CustomAuthenticationForm
    ), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]
