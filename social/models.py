from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Peluqueria(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	nombre_de_la_peluqueria = models.CharField(max_length=150, blank=False, null=False, default='Nombre de la peluqueria')
	image = models.ImageField(default='batman.png')
	email = models.EmailField(max_length=150, blank=False, null=False)
	telefono = models.CharField(max_length=13, blank=True, null=True)
	provincia = models.CharField(max_length=100, blank=False, null=False)
	municipio = models.CharField(max_length=100, blank=False, null=False)
	direccion = models.CharField(max_length=150, blank=False, null=False)

	cita_previa = models.BooleanField(default=False)
	servicio_a_domicilio = models.BooleanField(default=False)

	def __str__(self):
		return f'Peluquería de {self.user.username}'





