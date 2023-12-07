from django.db import models

class Productos(models.Model):
    Nombre= models.CharField(max_length=50)
    Precio=models.IntegerField()
    Stock=models.IntegerField()
    Imagen=models.CharField(max_length=200)
