from rest_framework import serializers
from .models import Productos


class ProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model= Productos
        fields=("id","Nombre","Precio","Stock","Imagen")