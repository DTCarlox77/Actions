from django.test import TestCase
from django.contrib.auth.models import User
from .models import Producto

class ProductoTestCase(TestCase):
	def setUp(self):
		# Crear usuarios para las pruebas
		self.usuario1 = User.objects.create_user(username='usuario1', password='password1')
		self.usuario2 = User.objects.create_user(username='usuario2', password='password2')

		# Configuración inicial antes de cada prueba
		Producto.objects.create(nombre="Producto1", precio=100, proveedor=self.usuario1, descripcion='')
		Producto.objects.create(nombre="Producto2", precio=200, proveedor=self.usuario2, descripcion='')

	def test_producto_nombre(self):
		# Prueba para verificar el nombre del producto
		producto1 = Producto.objects.get(nombre="Producto1")
		producto2 = Producto.objects.get(nombre="Producto2")
		self.assertEqual(producto1.nombre, "Producto1")
		self.assertEqual(producto2.nombre, "Producto2")

	def test_producto_precio(self):
		# Prueba para verificar el precio del producto
		producto1 = Producto.objects.get(nombre="Producto1")
		producto2 = Producto.objects.get(nombre="Producto2")
		self.assertEqual(producto1.precio, 100)
		self.assertEqual(producto2.precio, 200)

	def test_producto_usuario(self):
		# Prueba para verificar el usuario del producto
		producto1 = Producto.objects.get(nombre="Producto1")
		producto2 = Producto.objects.get(nombre="Producto2")
		self.assertEqual(producto1.proveedor.username, "usuario1")
		self.assertEqual(producto2.proveedor.username, "usuario2")