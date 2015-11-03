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
        return render(request, 'home.html', {'titulo': titulo, 'nombre': nombre})

class UserController(View):
    def get(self, request):
        titulo = "Inicio"
        nombre = "Agustin"
        return render(request, 'user.html', {'titulo': titulo, 'nombre': nombre})


class TestController(View):
    def get(self, request):
        titulo = "hola"
        return render(request, 'test.html', {'titulo': titulo})

