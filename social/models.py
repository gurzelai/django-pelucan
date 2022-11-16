from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Peluqueria(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='batman.png')
	email = models.EmailField(max_length=150, blank=False, null=False)
	telefono = models.CharField(max_length=13, blank=True, null=True)
	provincia = models.CharField(max_length=100, blank=False, null=False)
	municipio = models.CharField(max_length=100, blank=False, null=False)
	direccion = models.CharField(max_length=150, blank=False, null=False)

	def __str__(self):
		return f'Perfil de {self.user.username}'








