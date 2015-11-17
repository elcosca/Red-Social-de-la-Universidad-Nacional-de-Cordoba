from django.shortcuts import render
from django.views.generic import View
from coreF.models import *
## Create your views here.


class LoginController(View):
    def get(self, request):
        titulo = "Red Social Universidad Nacional de Cordoba"
        return render(request, 'login.html', {'titulo': titulo})


class HomeController(View):
    def get(self, request):
        titulo = "Inicio"
        nombre = "Agustin"
        publicaciones = Publicacion.objects.all()
#        mens_no_leidos = Mensaje.object.filter(leido=False)
        return render(request, 'home.html', {'titulo': titulo, 'nombre': nombre, 'publicaciones': publicaciones})


class Mensajes(View):
    def get(self, request):
#        titulo = "Mensajes Privados"
#        mensajes = Mensaje.objects.all()
#        mens_no_leidos = Mensaje.object.filter(leido=False)


#class UserController(View):
#    def get(self, request):
        titulo = "Inicio"
        nombre = "Agustin"
        return render(request, 'user.html', {'titulo': titulo, 'nombre': nombre})


class TestController(View):
    def get(self, request):
        titulo = "hola"
        return render(request, 'test.html', {'titulo': titulo})


class MensajeVerController(View):

#    def post(self, request):
#        id_mensaje = request.POST("")
        mensaje = Mensaje
