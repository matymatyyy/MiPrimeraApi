from .models import Productos
from rest_framework import viewsets, permissions
from .serializers import ProductoSerializers


class ProductosViewSets(viewsets.ModelViewSet):
    queryset=Productos.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class= ProductoSerializers