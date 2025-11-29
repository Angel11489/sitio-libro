from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy 
# Importar las clases de vistas de autenticación que necesitas
from django.contrib.auth.views import (
    PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView
) 
from .forms import RegistroForm, LoginForm, CustomPasswordResetForm, CustomSetPasswordForm

User = get_user_model()

def index(request):
    return render(request, 'Sitio web.html') 
def sitio_web(request):
    return render(request, 'Sitio web.html') 

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')  
    else:
        form = RegistroForm()
    
    return render(request, 'registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user() 
            if user is not None:
                login(request, user)
                return redirect('bienvenida') 
    else:
        form = LoginForm()
        
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login') 


class CustomPasswordResetView(PasswordResetView):
    template_name = 'reset_password.html' 
    form_class = CustomPasswordResetForm
    email_template_name = 'password_reset_email.html' 
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'reset_password_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('password_reset_complete')