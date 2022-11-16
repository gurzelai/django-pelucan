from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def feed(request):

	return render(request, 'social/feed.html', {})

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

def profile(request, username=None):
	current_user = request.user
	if username==None and request.user.is_authenticated == False:
		return HttpResponse("no estás logeado")
	if username and username != current_user.username:
		user = User.objects.get(username=username) #el perfil de otra persona
		
	else:
		user = current_user
		username = user.username

	return render(request, 'social/profile.html', {'user':user, 'username':username})