from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Producto(models.Model):
    
    nombre = models.CharField(max_length=20)
    precio = models.DecimalField(decimal_places=2, max_digits=10)
    proveedor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ProveedorFruta')
    descripcion = models.TextField()
    
    def __str__(self) -> str:
        return f'Producto: {self.nombre} a {self.precio} $.'