from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import UserForm, PostForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def feed(request):
	posts = Post.objects.all()

	context = { 'posts': posts}
	return render(request, 'social/feed.html', context)

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

@login_required
def post(request):
	current_user = get_object_or_404(User, pk=request.user.pk)
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = current_user
			post.save()
			messages.success(request, 'Post enviado')
			return redirect('profile')
	else:
		form = PostForm()
	return render(request, 'social/post.html', {'form' : form })

def profile(request, username=None):
	current_user = request.user
	if username==None and request.user.is_authenticated == False:
		return HttpResponse("no estás logeado")
	if username and username != current_user.username:
		user = User.objects.get(username=username) #el perfil de otra persona
		posts = user.posts.all()
	else:
		posts = current_user.posts.all() #el perfil de mi persona
		user = current_user
		username = user.username

	return render(request, 'social/profile.html', {'user':user, 'posts':posts, 'username':username})


def follow(request, username):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user
	rel = Relationship(from_user=current_user, to_user=to_user_id)
	rel.save()
	messages.success(request, f'sigues a {username}')
	return redirect('feed')

def unfollow(request, username):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user.id
	rel = Relationship.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
	rel.delete()
	messages.success(request, f'Ya no sigues a {username}')
	return redirect('feed')