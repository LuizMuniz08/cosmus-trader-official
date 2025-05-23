from django.db import models
from django.contrib.auth.models import User

class Operacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_operacao = models.DateTimeField(auto_now_add=True)
    tipo_operacao = models.CharField(max_length=10, choices=[('compra', 'Compra'), ('venda', 'Venda')])
    entrada = models.DecimalField(max_digits=10, decimal_places=2)
    stop = models.DecimalField(max_digits=10, decimal_places=2)
    alvo = models.DecimalField(max_digits=10, decimal_places=2)
    resultado = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=10, choices=[('aberta', 'Aberta'), ('fechada', 'Fechada'), ('cancelada', 'Cancelada')], default='aberta')
    lucro_prejuizo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):