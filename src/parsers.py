# -*- coding:utf-8 -*-
'''
Created on 26 ene 2022

@author: willi
'''
from datetime import datetime
def parsea_booleano(cadena):
    res=True
    cadena= cadena.upper()
    if cadena== 'GANADO':
        res=True
    elif cadena =='PERDIDO':
        res = False
    return res

def parsea_fecha(cadena):
    return datetime.strptime(cadena, '%d/%m/%Y').date()