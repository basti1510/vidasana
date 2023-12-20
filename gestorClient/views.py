from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from gestorClient.models import *
from .forms import newClientForm
import datetime
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def is_admin(user):
    return user.is_superuser

def is_not_admin(user):
    value = not(user.is_superuser)
    return value

#------------------------------------------------------------------------------#
def createClient(request):
    if request.method == "POST":
        form = newClientForm(request.POST, request.FILES)
        if form.is_valid():   
            instance = form.save(commit=False)
            instance.autor = request.user
            instance.save()
            form.save()
            form.cleaned_data['nombre'] = ''
            form.cleaned_data['rut'] = ''
            form.cleaned_data['nacimiento'] = ''
            form.cleaned_data['edad'] = ''
            form.cleaned_data['telefono'] = ''
            form.cleaned_data['estatura'] = ''
            form.cleaned_data['peso'] = ''
            form.cleaned_data['imc'] = ''
            form.cleaned_data['talla'] = ''
            form.cleaned_data['cintura'] = ''
            form.cleaned_data['presion'] = ''
            form.cleaned_data['f_cardiaca'] = ''
            form.cleaned_data['p_grasa'] = ''
            print("Cliente agregado correctamente")
            return HttpResponseRedirect(reverse('dashboard'))
            
    else:
        form = newClientForm()        
    data = {'form': form,
            'titulo_menu': 'Crear Cliente',
            'boton': 'Crear Cliente'
            }
    return render(request, 'gestorClient/createClient.html', data)

#@user_passes_test(is_admin)
def readClient(request):
    clients = Client.objects.all()
    data = {
        'clients' : clients
    }
    return render(request, 'gestorClient/listaClient.html', data)

def editClient(request, id):
    client = Client.objects.get(id = id)
    form = newClientForm(instance=client)
    if request.method == "POST":
        form = newClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            if request.user.is_superuser or request.user.is_staff:
                return HttpResponseRedirect(reverse('listaClient'))
                            
    data = {'form': form,
            'titulo' : 'Editar Cliente',
            'boton' : 'Aplicar cambios'
            }
    return render(request, 'gestorClient/createClient.html', data)

#@user_passes_test(is_admin)
def delClient(request, id):
    client = Client.objects.get(id = id)
    client.delete()
    return HttpResponseRedirect(reverse('listaClient'))

#------------------------------------------------------------------------------#
def marcarAsist(request, id):
    client = Client.objects.get(id = id)
    date= datetime.datetime.now()
    instance = Asist(fecha= date, id_Cliente= client)
    instance.save()
    
    return HttpResponseRedirect(reverse('asistClient'))

def asistClient(request):
    clients = Client.objects.all()
    data = {
        'clients' : clients
    }
    return render(request, 'gestorClient/asistClient.html', data)

def readAsist(request, id):
    client = Client.objects.get(id = id)
    asists = Asist.objects.filter(id = id).count()
    
    data = {
        'client' : client,
        'asists' : asists
    }
    
    return render(request, 'gestorClient/readAsist.html', data)
