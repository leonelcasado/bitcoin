# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import requests
from datetime import datetime
import time
from bitcoin.backend.historico.historico_bitcoin import gravar
#==================================================
def consultar_indicadores_bitcoin():
    try:
        #==================================================
        r=requests.get("https://foxbit.com.br/ticker/ticker.php")
        json_data = r.json()
        #print(json_data)
        #==================================================
        print('=======================================')
        print('Início:',datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        print('Alta:%s' % json_data['high'])
        print('Baixa:%s' % json_data['low'])
        print('Compra:%s' % json_data['buy'])
        print('Venda:%s' % json_data['sell'])
        print('Volume:%s' % json_data['vol'])        
        #==================================================
        gravar(json_data['high'],json_data['low'],json_data['buy'],json_data['sell'],json_data['vol'])
        #==================================================
    except Exception as e:
        print(e)
#==================================================
def execute():
    while(True):
        consultar_indicadores_bitcoin()
        time.sleep(5)
#==================================================
execute()
#==================================================