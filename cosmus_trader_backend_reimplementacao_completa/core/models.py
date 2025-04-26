from django.db import models

class Operacao(models.Model):
    STATUS_CHOICES = [
        ('ATIVA', 'Ativa'),
        ('FINALIZADA', 'Finalizada'),
    ]
    
    # Campos principais
    entrada = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço de Entrada')
    stop = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço de Stop')
    alvo = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço de Alvo')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ATIVA', verbose_name='Status da Operação')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name='Última Atualização')

    def __str__(self):
        return f"Operação {self.id} - {self.status}"

    class Meta:
        verbose_name = "Operação"
        verbose_name_plural = "Operações"
