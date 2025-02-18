# core/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import RegisterForm

def landing_view(request):
    return render(request, 'landing.html')

@login_required(login_url='/login-required/')
def dashboard_view(request):
    return render(request, 'dashboard.html', {'user': request.user})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def custom_logout(request):
    logout(request)
    return redirect('/')

def login_required_error(request):
    return render(request, 'login_required.html')

class CustomLoginView(LoginView):
    template_name = 'login.html'

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password. Please try again.")
        return super().form_invalid(form)