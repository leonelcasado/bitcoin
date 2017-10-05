# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import requests
from datetime import datetime
import time
import pymysql
from bitcoin import settings
#==================================================
def gravar(val_alta,val_baixa,val_compra,val_venda,val_volume):
    try:
        conn = pymysql.connect(host=settings.HOST_DB,port=3306, user=settings.USER_DB, passwd=settings.PASSWORD_DB, db=settings.NAME_DB)
        cur = conn.cursor()
        data_criacao=datetime.datetime.today()
        valor_diferenca_alta_baixa=val_alta-val_baixa
        valor_diferenca_compra_baixa=val_compra-val_baixa
        valor_diferenca_venda_baixa=val_venda-val_baixa
        sql="insert into historico_historico(valor_alta,valor_baixa,valor_compra,valor_venda,valor_volume,data_criacao,valor_diferenca_alta_baixa,valor_diferenca_compra_baixa,valor_diferenca_venda_baixa)values('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (val_alta,val_baixa,val_compra,val_venda,val_volume,data_criacao,valor_diferenca_alta_baixa,valor_diferenca_compra_baixa,valor_diferenca_venda_baixa)
        #print(sql)
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        #print(e)
        conn.rollback()
    
    cur.close()
    conn.close()
#==================================================
def consultar_indicadores_bitcoin():
    try:
        #==================================================
        r=requests.get("https://foxbit.com.br/ticker/ticker.php")
        json_data = r.json()
        #print(json_data)
        #==================================================
        print('=======================================')
        print('Início:',datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
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