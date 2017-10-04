# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from bitcoin.backend.historico.models import Historico
#===================================================================
class HistoricoSerializer(serializers.ModelSerializer):
    #===============================================================
    class Meta:
        model = Historico
        fields=('id','valor_baixa','valor_alta','valor_diferenca_alta_baixa','valor_compra','valor_diferenca_compra_baixa','valor_venda','valor_diferenca_venda_baixa','valor_volume','data_criacao')
    #===============================================================
#===================================================================
