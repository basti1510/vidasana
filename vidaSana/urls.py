"""
URL configuration for vidaSana project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from gestorUser.views import *
from gestorClient.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', userIndex, name="dashboard"),
    path('signUp/', signUp, name='signUp'),
    path('listaUsuarios/', readUsers, name='listaUsuarios'),
    path('editUser/<int:id>', editUser, name='editUser'),
    path('delUser/<int:id>', delUser, name='delUser'),
    path('addClient/', createClient, name='addClient'),
    path('listaClient/', readClient, name='listaClient'),
    path('editClient/<int:id>', editClient, name='editClient'),
    path('delClient/<int:id>', delClient, name='delClient'),
    path('asistClient/', asistClient, name='asistClient'),
    path('marcarAsist/<int:id>', marcarAsist, name='marcarAsist'),
    path('readAsist/<int:id>', readAsist, name='readAsist'),
]
