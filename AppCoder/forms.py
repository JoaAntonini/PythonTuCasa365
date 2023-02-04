

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SillonFormulario(forms.Form):    
    sillon = forms.CharField()
    precio = forms.IntegerField()
    stock =  forms.IntegerField()

class MesaFormulario(forms.Form):    
    mesa = forms.CharField()
    precio = forms.IntegerField()
    color = forms.CharField()
    stock =  forms.IntegerField()
    
class LamparaFormulario(forms.Form):    
    lampara = forms.CharField()
    precio = forms.IntegerField()
    tamaño = forms.CharField()
    stock =  forms.IntegerField()
    
    
    
class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre")
    last_name =  last_name = forms.CharField(label="Apellido")
    username = forms.CharField(label="Usuario")
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields =  ['first_name','last_name', 'username', 'email', 'password1', 'password2'] 

class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']

