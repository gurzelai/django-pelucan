from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
	path('', views.index, name='index'),
	path('peluqueria/', views.peluqueria, name='peluqueria'),
	path('peluqueria/<str:username>/', views.peluqueria, name='peluqueria'),  #ver perfil de otro http://127.0.0.1:8000/profile/goku/
	path('register/', views.register, name='register'),
	path('login/', LoginView.as_view(template_name='social/login.html'), name='login'),
	path('logout/', LogoutView.as_view(template_name='social/logout.html'), name='logout'),
	path('peluquerias/', views.peluquerias, name='peluquerias'),
	path('peluquerias-a-domicilio/', views.peluquerias_a_domicilio, name='peluquerias_a_domicilio'),
	
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)