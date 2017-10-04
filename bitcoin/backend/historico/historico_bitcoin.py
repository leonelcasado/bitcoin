# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import pymysql
import datetime
from bitcoin import settings
#===============================================
'''
def consultar_teste():
    try:
        conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='escolasa_01')
        cur = conn.cursor()
        cur.execute("SELECT * FROM sia_usuario")
        print(cur.description)
        for row in cur:
            print(row)

        cur.close()
        conn.close()
    except Exception as e:
        print(e)
'''        
#===============================================
def consultar_baixa_alta():
    id=None
    val_baixa=None
    val_alta=None
    dat_baixa=None
    dat_alta=None
    lista_baixa=[]
    lista_alta=[]
    try:
        #conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='bitcoin')
        conn = pymysql.connect(host=settings.HOST_DB,port=3306, user=settings.USER_DB, passwd=settings.PASSWORD_DB, db=settings.NAME_DB)
        cur = conn.cursor()
        cur.execute("select a.id,a.valor_baixa,a.valor_alta,a.data_criacao from historico_historico a order by 1 desc")
        #print(cur.description)
        for row in cur:
            #print(row)
            if (val_baixa==None):
                id=row[0]
                val_baixa=row[1]
                dat_baixa=row[3]
                lista_baixa.append((id,val_baixa,dat_baixa))
            
            elif (row[1]!=val_baixa):
                id=row[0]
                val_baixa=row[1]
                dat_baixa=row[3]
                lista_baixa.append((id,val_baixa,dat_baixa))


            if (val_alta==None):
                id=row[0]
                val_alta=row[2]
                dat_alta=row[3]
                lista_alta.append((id,val_alta,dat_alta))
            
            elif (row[2]!=val_alta):
                id=row[0]
                val_alta=row[2]
                dat_alta=row[3]
                lista_alta.append((id,val_alta,dat_alta))
                
        #print(lista_baixa)
        #print(lista_alta)
        cur.close()
        conn.close()
    except Exception as e:
        print(e)
        
    return lista_baixa,lista_alta
#===============================================
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
#===============================================