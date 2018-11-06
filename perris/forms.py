from django import forms
from .models import Perros_Rescatados
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class Perro_RescatadoForm(forms.ModelForm):
	class Meta:
		model=Perros_Rescatados
		fields=('fotografia_perro','nombre_perro' , 'raza_predominante' , 'descripcion','estado', )	






class CustomCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, label="Nombre")
    last_name = forms.CharField(required=True, label="Apellido")

    class Meta:
        model = User
        fields = ('username',
        'first_name',
         'last_name',
         'email',
         'password1',
         'password2')
         