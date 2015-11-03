from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Mensaje(models.Model):
    remitente = models.ForeignKey(User, related_name="remitente")
    destinatario = models.ForeignKey(User, related_name="destinatario")
    contenido = models.CharField(max_length=2000)


class Comentario(models.Model):
    contenido = models.CharField(max_length=2000)


class Publicaciones(models.Model):
    contenido = models.CharField(max_length=2000)
    comentarios = models.ForeignKey(Comentario)


class Notificacion(models.Model):
    notificacion = models.ForeignKey(Publicaciones)
