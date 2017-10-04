# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.db import models
#======================================================================================
class Investidor(models.Model):
    nome = models.CharField(max_length=100,unique=True,blank=False,null=False)
    valor_investido = models.DecimalField(max_digits=10,decimal_places=2,blank=False,null=False)
    valor_bitcoin = models.DecimalField(max_digits=20,decimal_places=8,blank=False,null=False)
    data_investimento=models.DateField(blank=False,null=False)
    data_criacao=models.DateTimeField(auto_now_add=True)
    #==================================================================================
#======================================================================================
