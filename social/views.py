from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def index(request):

	return render(request, 'social/index.html', {})

def peluquerias(request):

	peluquerias = Peluqueria.objects.all()
	context = { 'peluquerias': peluquerias}

	return render(request, 'social/peluquerias.html', context)

def peluquerias_a_domicilio(request):

	peluquerias = Peluqueria.objects.filter(servicio_a_domicilio=True)
	context = { 'peluquerias': peluquerias}
	
	return render(request, 'social/peluquerias.html', context)

def register(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, f'Usuario {username} creado')
			return redirect('feed') #aquí habría que poner la pagina de editar perfil
	else:
		form = UserForm()

	context = { 'form' : form }
	return render(request, 'social/register.html', context)

def peluqueria(request, username=None):
	current_user = request.user
	if username==None and request.user.is_authenticated == False: #no le vamos a dejar en "Tu perfil" si no estás logeado
		return HttpResponse("no estás logeado")
	if username and username != current_user.username: #el perfil de otra persona
		user = User.objects.get(username=username)
		tu_perfil = False
	else: #si estás entrando a ver tu perfil
		user = current_user
		username = user.username
		tu_perfil = True
	return render(request, 'social/profile.html', {'user':user, 'username':username, 'tu_perfil':tu_perfil})