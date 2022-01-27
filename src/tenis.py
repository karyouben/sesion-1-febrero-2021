# -*- coding:utf-8 -*-
'''
Created on 26 ene 2022

@author: willi
'''
from collections import namedtuple, Counter
import csv
import statistics
from parsers import *

Partido = namedtuple('Partido', 'fecha, rival, superficie, duracion, juegos_ganados, juegos_perdidos, ganado')
def lee_fichero(fichero):
    with open(fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        res= []
        for fecha, rival, superficie, duracion, juegos_ganados, juegos_perdidos, ganado in lector:
            tupla = Partido(parsea_fecha(fecha), rival, superficie, int(duracion), int(juegos_ganados), int(juegos_perdidos), parsea_booleano(ganado))
            res.append(tupla)
    return res

def desviaciones_media(registros,n):
    res = sum(t.duracion for t in registros)/len(registros)
    return [abs(t.duracion-res, t) for t in registros if abs(t.duracion-res)>n]  

def diccionario_diferencia_juegos_superficie(registros,n=3):
    partidos_superficie = diccionario_agrupa_superficie(registros)
    dicc = {}
    for c in partidos_superficie:
        diferencia = sorted(registros, key= lambda x:abs(x.juegos_ganados-x.juegos_perdidos),reverse = True)[:n]
        dicc[c]=[t.fecha for t in diferencia]
    return dicc 

def diccionario_agrupa_superficie(registros):
    dicc = {}
    for t in registros:
        clave = t.superficie
        if clave in dicc:
            dicc[clave].append(t)
        else:
            dicc[clave]= t
    return dicc

def rival_mayor_porcentaje_victorias(registros,superficie):
    dicc = agrupa_por_rival(registros, superficie)
    dicc_porc = {clave:calcular_porcentaje(valor) for clave, valor in dicc.items()}
    return max(dicc_porc.items(), key = lambda x:x[1])

    
def agrupa_por_rival(registros,superficie):
    dicc = {}
    for t in registros:
        if t.superficie == superficie:
            clave= t.rival
            if clave in dicc:
                dicc[clave].append(t)
            else:
                dicc[clave]= [t]
    return dicc
        
def calcular_porcentaje(registros):
    partidos = len(registros)
    victorias = len([t for t in registros if t.ganado == True])
    return (victorias/partidos)*100
    