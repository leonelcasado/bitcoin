# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.db import models
#======================================================================================
class Historico(models.Model):
    valor_baixa = models.DecimalField(max_digits=10,decimal_places=2,blank=False,null=False)
    valor_alta = models.DecimalField(max_digits=10,decimal_places=2,blank=False,null=False)
    valor_diferenca_alta_baixa = models.DecimalField(max_digits=10,decimal_places=2,blank=False,null=False)
    valor_compra = models.DecimalField(max_digits=10,decimal_places=2,blank=False,null=False)
    valor_diferenca_compra_baixa = models.DecimalField(max_digits=10,decimal_places=2,blank=False,null=False)
    valor_venda = models.DecimalField(max_digits=10,decimal_places=2,blank=False,null=False)
    valor_diferenca_venda_baixa = models.DecimalField(max_digits=10,decimal_places=2,blank=False,null=False)
    valor_volume = models.DecimalField(max_digits=20,decimal_places=8,blank=False,null=False)
    data_criacao=models.DateTimeField(blank=False,null=False)
    #==================================================================================
    class Meta:
        ordering = ('-data_criacao',)
        unique_together = (('valor_baixa','valor_alta','valor_compra','valor_venda','valor_volume'),)
    #==================================================================================
#======================================================================================
