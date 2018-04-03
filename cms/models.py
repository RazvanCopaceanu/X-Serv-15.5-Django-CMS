from django.db import models

class Pages(models.Model):
    nombre = models.CharField(max_length=32)
    pagina = models.TextField()
    def __str__(self):
        return self.nombre
