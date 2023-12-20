from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from gestorClient.models import *


#______________________CLIENTES___________________________________#
class newClientForm(forms.Form):
    nombre = forms.CharField(label='Nombre')
    rut = forms.CharField(label='RUT')
    nacimiento = forms.DateTimeField(label='Nacimiento')
    edad = forms.IntegerField(label='Edad')
    telefono = forms.CharField(label='Telefono')
    estatura = forms.IntegerField(label='Estatura')
    peso = forms.IntegerField(label='Peso')
    imc = forms.DecimalField(label='IMC')
    talla = forms.IntegerField(label='Talla')
    cintura = forms.IntegerField(label='Cintura')
    presion = forms.IntegerField(label='Presion')
    f_cardiaca = forms.IntegerField(label='Frecuencia Cardiaca')
    p_grasa = forms.IntegerField(label='Porcentaje de Grasa')
    
    
    nombre.widget.attrs['class'] = 'form-control'
    rut.widget.attrs['class'] = 'form-control'
    nacimiento.widget.attrs['class'] = 'form-control'
    edad.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'
    estatura.widget.attrs['class'] = 'form-control'
    peso.widget.attrs['class'] = 'form-control'
    imc.widget.attrs['class'] = 'form-control'
    talla.widget.attrs['class'] = 'form-control'
    cintura.widget.attrs['class'] = 'form-control'
    presion.widget.attrs['class'] = 'form-control'
    f_cardiaca.widget.attrs['class'] = 'form-control'
    p_grasa.widget.attrs['class'] = 'form-control'
    
class newClientForm(forms.ModelForm):
    nombre = forms.CharField(label='Nombre')
    rut = forms.CharField(label='RUT')
    nacimiento = forms.DateTimeField(label='Nacimiento')
    edad = forms.IntegerField(label='Edad')
    telefono = forms.CharField(label='Telefono')
    estatura = forms.IntegerField(label='Estatura')
    peso = forms.IntegerField(label='Peso')
    imc = forms.DecimalField(label='IMC')
    talla = forms.IntegerField(label='Talla')
    cintura = forms.IntegerField(label='Cintura')
    presion = forms.IntegerField(label='Presion')
    f_cardiaca = forms.IntegerField(label='Frecuencia Cardiaca')
    p_grasa = forms.IntegerField(label='Porcentaje de Grasa')
    
    
    nombre.widget.attrs['class'] = 'form-control'
    rut.widget.attrs['class'] = 'form-control'
    nacimiento.widget.attrs['class'] = 'form-control'
    edad.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'
    estatura.widget.attrs['class'] = 'form-control'
    peso.widget.attrs['class'] = 'form-control'
    imc.widget.attrs['class'] = 'form-control'
    talla.widget.attrs['class'] = 'form-control'
    cintura.widget.attrs['class'] = 'form-control'
    presion.widget.attrs['class'] = 'form-control'
    f_cardiaca.widget.attrs['class'] = 'form-control'
    p_grasa.widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = Client
        fields = '__all__'
