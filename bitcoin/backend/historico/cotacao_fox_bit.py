import requests
from bitcoin.backend.historico.historico_bitcoin import gravar
from datetime import datetime
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
#consultar_indicadores_bitcoin()
#==================================================