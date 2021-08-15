from django.urls import path
from django.utils.regex_helper import normalize
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear/', views.crearPost, name='crear'),
    path('registrarse/', views.registrarUsuario, name='register'),
    path('post/<int:pk>', views.verPost, name='post'),
    path('actualizar/<int:pk>', views.actualizarPost, name='actualizar'),
    path('eliminar/<int:pk>', views.eliminarPost, name='eliminar'),
    path('like/<int:pk>', views.darlike, name='dar_like')
]