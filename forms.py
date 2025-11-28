from django import forms
from .models import Usuario 
from django.contrib.auth.hashers import check_password 
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

# 1. RegistroForm
class RegistroForm(forms.ModelForm):
    # Añadimos 'password' para manejar la contraseña de forma estándar con ModelForms
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Escribe aquí tu contraseña'}))

    class Meta:
        model = User
        fields = ['nombre', 'correo', 'password']
        
    def save(self, commit=True):
        # Usamos el manager personalizado para crear el usuario, que hashea la contraseña.
        user = User.objects.create_user(
            correo=self.cleaned_data['correo'],
            nombre=self.cleaned_data['nombre'],
            password=self.cleaned_data['password']
        )
        return user

# 2. LoginForm (Simplificado para usar authenticate correctamente)
class LoginForm(forms.Form):
    correo = forms.EmailField(label="Correo electrónico", widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Escribe aquí tu Gmail'}))
    contraseña = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Escribe aquí tu contraseña'}))

    def clean(self):
        cleaned_data = super().clean()
        correo = cleaned_data.get('correo')
        contraseña = cleaned_data.get('contraseña')

        if correo and contraseña:
            # Intenta autenticar usando el campo `correo` como username
            self.user_cache = authenticate(username=correo, password=contraseña)
            
            if self.user_cache is None:
                raise forms.ValidationError("Correo o contraseña incorrectos.")
            
        return cleaned_data
    
    def get_user(self):
        return getattr(self, 'user_cache', None)


# 3. CustomSetPasswordForm (Corregido el método __init__)
class CustomSetPasswordForm(SetPasswordForm):
    # ... (campos new_password1 y new_password2)
    
    def __init__(self, user, *args, **kwargs): # CORREGIDO: Usar __init__
        super().__init__(user, *args, **kwargs) 
        self.user = user