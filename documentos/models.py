from django.db import models

class Documento(models.Model):
    nombre = models.CharField(max_length=200)
    contenido = models.TextField()
    resultado = models.CharField(max_length=200)
    def __unicode__(self):
    	return self.nombre

