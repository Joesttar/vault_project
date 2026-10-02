from django.db import models

# Create your models here.
class Team(models.Model):
    nombre =  models.CharField(max_length=20, unique=True, help_text="Nombre del equipo o departamento")
    descripcion = models.TextField(blank=True, null=True, help_text="Descripcion de las responsabilidades del equipo")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"
        ordering = ['nombre']

    def __str__(name):
        return self.name