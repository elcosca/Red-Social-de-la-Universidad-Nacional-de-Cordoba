from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Mensaje(models.Model):
    remitente = models.ForeignKey(User, related_name="remitente")
    destinatario = models.ForeignKey(User, related_name="destinatario")
    contenido = models.CharField(max_length=2000)
    leido = models.BooleanField(default=False)


class Comentario(models.Model):
    contenido = models.CharField(max_length=2000)


class Publicacion(models.Model):
    contenido = models.CharField(max_length=2000)
    comentarios = models.ForeignKey(Comentario)
#    creador = models.ForeignKey(User)

    def __unicode__(self):
        name = self.creador.get_full_name()
        return name

class Notificacion(models.Model):
    notificacion = models.ForeignKey(Publicacion)
