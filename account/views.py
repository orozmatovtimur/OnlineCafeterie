from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import User
from .forms import NewUserForm

class RegisterView(CreateView):
    model = User
    form_class = NewUserForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('home')


class SignInView(LoginView):

    template_name = '/registration/login.html'
    success_url = reverse_lazy('home')
