from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Client(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=50)
    nacimiento = models.DateTimeField()
    edad = models.IntegerField()
    telefono = models.CharField(max_length=15)
    estatura = models.IntegerField()
    peso = models.IntegerField()
    imc = models.DecimalField(max_digits=5, decimal_places=2)
    talla = models.IntegerField()
    cintura = models.IntegerField()
    presion = models.IntegerField()
    f_cardiaca = models.IntegerField()
    p_grasa = models.IntegerField()
    
    def __str__(self):
        return self.nombre
    
    
class Asist(models.Model):
     fecha = models.DateTimeField()
     id_Cliente = models.ForeignKey(Client, on_delete=models.CASCADE)   