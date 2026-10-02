import os
from django.db import models
from django.contrib.auth.models import User
from cryptography.fernet import Fernet
from teams.models import Team

# Create your models here.


def obtener_cifrado():
    llave = os.getenv('ENCRYPTION_KEY')
    return Fernet(llave.encode())


class Secret(models.Model):
    ENTERNOS = [
        ('DEV', 'Desarrollo'),
        ('STG', 'Staging'),
        ('PRD', 'Produccion')
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    valor_cifrado = models.TextField()
    entorno = models.CharField(max_length=3, choices=ENTERNOS, default='DEV')
    creador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='secretos_creados')
    equipos = models.ManyToManyField(Team, related_name='secretos_creados', blank=True)
    
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def set_valor_secreto(self, texto_plano: str):
        cifrador = obtener_cifrado()
        bytes_cifrador = cifrador.encrypt(texto_plano.encode())
        self.valor_cifrado = bytes_cifrador.decode() 

    def get_valor_secreto(self) -> str:
        cifrador = obtener_cifrado()
        bytes_decifrados = cifrador.decrypt(self.valor_cifrado.encode())
        return bytes_cifrador.decode()

    def __str__(self):
        return f"{self.nombre} ({self.entorno})"
        