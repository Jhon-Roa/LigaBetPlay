import os
from tabulate import tabulate
import operator

dict(equipo = {})

def AddTeam(lstEquipos : dict):
    nombre = input('Ingrese el nombre del Equipo :')
    nombre_c = nombre.capitalize()
    pj= 0
    pg= 0
    pp= 0
    pe= 0
    gf= 0
    gc= 0
    tp= 0
    equipo= {
        'nombre' : nombre_c,
        'pj' : pj,
        'pg' : pg,
        'pp' : pp,
        'pe' : pe,
        'gf' : gf,
        'gc' : gc,
        'tp' : tp
    }
    lstEquipos.update({nombre_c : dict(equipo)})
    
def ValidateTeam(lstEquipos: dict, nombre):
    return bool(lstEquipos.get(nombre,''))
    
def DelTeam(lstEquipos : dict):
    nombre = input('Ingrese nombre del equipo a borrar')
    nombre_c = nombre.capitalize()
    if ValidateTeam(lstEquipos, nombre_c):
        lstEquipos.pop(nombre)
    else:
        print('equipo no encontrado')

def ViewTeam(lstEquipos : dict):
    a = dict(sorted(lstEquipos.items(), key= lambda item: item[1]['tp'], reverse=True))
    os.system('pause')
    os.system('cls')
    titulo= """
    +++++++++++++++++++++++++++++++++++++++
    + TABLA DE CLASIFICACION LIGA BETPLAY +
    +++++++++++++++++++++++++++++++++++++++
    """ 
    print(titulo)
    info= []
    for key, values in a.items():
        info.append(values)
        os.system('cls')
        print(tabulate(info, headers= 'keys', tablefmt='grid'))
    os.system('pause')