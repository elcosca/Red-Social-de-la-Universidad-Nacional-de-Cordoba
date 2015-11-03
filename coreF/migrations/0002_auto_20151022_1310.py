# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('coreF', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contenido', models.CharField(max_length=2000)),
            ],
        ),
        migrations.RenameField(
            model_name='mensaje',
            old_name='mensaje',
            new_name='contenido',
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='remitente',
            field=models.ForeignKey(related_name='remitente', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='comentarios',
            field=models.ForeignKey(to='coreF.Comentario'),
        ),
    ]
