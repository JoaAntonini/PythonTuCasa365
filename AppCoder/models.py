from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sillon(models.Model):
    nombre=models.CharField(max_length=40)
    precio = models.IntegerField()    
    stock = models.IntegerField() 
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Precio {self.precio} - Stock {self.stock}"

class Lamparas(models.Model):
    nombre=models.CharField(max_length=40)
    precio = models.IntegerField()    
    tamaño = models.CharField(max_length=40)
    stock =  models.IntegerField() 
    
    def __str__(self):        
            return f"Nombre: {self.nombre} - Precio {self.precio} - Tamaño {self.tamaño} - Stock {self.stock}"

class Mesas(models.Model):
    nombre=models.CharField(max_length=40)
    precio = models.IntegerField()    
    color= models.CharField(max_length=40)
    stock = models.IntegerField() 
    
    def __str__(self):
            return f"Nombre: {self.nombre} - Precio {self.precio} - Color {self.color} - Stock {self.stock}"
        

class Avatar(models.Model):
            
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    
    def __str__(self):
        return f"{self.user} - {self.imagen}"
    
    