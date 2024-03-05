import os

lstEquipos = {}
lstFechas = {}
opcion_l = {}
opcion_v = {}
fecha = {}
reportes = {}

def ValidateDate(lstEquipos: dict, nombre, reportes: dict):
    return bool(lstEquipos.get(nombre, ''))

def Addgame(lstEquipos: dict, lstFechas: dict, opcion_l: dict, opcion_v: dict, reportes: dict, counter: int = 1):
    msg = ''
    titulo = """
    +++++++++++++++++++++++++++
    + INGRESAR FECHA DE JUEGO +
    +++++++++++++++++++++++++++
    """
    print(titulo)

    for key, item in lstEquipos.items():
        print(key)

    if counter == 1:
        msg = 'Ingrese el equipo local'
        estado = 'L'
    else:
        msg = 'Ingrese el equipo visitante'
        estado = 'V'

    opcion = str(input(f'{msg}: '))
    opcion_c = opcion.capitalize()

    if ValidateDate(lstEquipos, opcion_c, reportes):
        goles = int(input(f"Ingrese goles marcados por {lstEquipos[opcion_c]['nombre']}"))
        fecha.update({opcion_c: {'nombre': lstEquipos[opcion_c]['nombre'], 'goles': goles, 'estado': estado}})

        if counter == 1:
            opcion_l['equipo'] = opcion_c
        else:
            opcion_v['equipo'] = opcion_c
    else:
        print('Ingrese un equipo válido')
        os.system('pause')
        Addgame(lstEquipos, lstFechas, opcion_l, opcion_v, reportes, counter)

    os.system('pause')
    counter += 1

    if counter <= 2:
        Addgame(lstEquipos, lstFechas, opcion_l, opcion_v, reportes, counter)
    else:
        NroFecha = input('Ingrese el número de fecha: ')
        lstFechas[NroFecha] = fecha

        local = opcion_l['equipo']
        visitante = opcion_v['equipo']

        lstEquipos[local]['gf'] += fecha[local]['goles']
        lstEquipos[local]['gc'] += fecha[visitante]['goles']
        lstEquipos[visitante]['gf'] += fecha[visitante]['goles']
        lstEquipos[visitante]['gc'] += fecha[local]['goles']

        if fecha[local]['goles'] > fecha[visitante]['goles']:
            lstEquipos[local]['pj'] += 1
            lstEquipos[local]['pg'] += 1
            lstEquipos[local]['tp'] += 3
            lstEquipos[visitante]['pj'] += 1
            lstEquipos[visitante]['pp'] += 1
        elif fecha[local]['goles'] < fecha[visitante]['goles']:
            lstEquipos[visitante]['pj'] += 1
            lstEquipos[visitante]['pg'] += 1
            lstEquipos[visitante]['tp'] += 3
            lstEquipos[local]['pj'] += 1
            lstEquipos[local]['pp'] += 1
        else:
            lstEquipos[visitante]['pj'] += 1
            lstEquipos[visitante]['pe'] += 1
            lstEquipos[visitante]['tp'] += 1
            lstEquipos[local]['pj'] += 1
            lstEquipos[local]['pe'] += 1
            lstEquipos[local]['tp'] += 1

        golesMax = 0
        nombreMax = ''

        if lstEquipos[opcion_l['equipo']]['gf'] > golesMax:
            golesMax = lstEquipos[opcion_l['equipo']]['gf']
            nombreMax = lstEquipos[opcion_l['equipo']]['nombre']

        if lstEquipos[opcion_v['equipo']]['gf'] > golesMax:
            golesMax = lstEquipos[opcion_v['equipo']]['gf']
            nombreMax = lstEquipos[opcion_v['equipo']]['nombre']

        reportes['MaxGoles']['nombre'] = nombreMax
        reportes['MaxGoles']['valor'] = golesMax
        
        tpMax = 0
        nombreMax = ''

        if lstEquipos[opcion_l['equipo']]['tp'] > tpMax:
            tpMax = lstEquipos[opcion_l['equipo']]['tp']
            nombreMax = lstEquipos[opcion_l['equipo']]['nombre']

        if lstEquipos[opcion_v['equipo']]['tp'] > tpMax:
            tpMax = lstEquipos[opcion_v['equipo']]['tp']
            nombreMax = lstEquipos[opcion_v['equipo']]['nombre']
            
        reportes['MaxPT']['nombre'] = nombreMax
        reportes['MaxPT']['valor'] = tpMax
        
        pgMax = 0
        nombreMax = ''

        if lstEquipos[opcion_l['equipo']]['pg'] > pgMax:
            pgMax = lstEquipos[opcion_l['equipo']]['pg']
            nombreMax = lstEquipos[opcion_l['equipo']]['nombre']

        if lstEquipos[opcion_v['equipo']]['pg'] > pgMax:
            pgMax = lstEquipos[opcion_v['equipo']]['pg']
            nombreMax = lstEquipos[opcion_v['equipo']]['nombre']
            
        reportes['MaxPG']['nombre'] = nombreMax
        reportes['MaxPG']['valor'] = pgMax
        
        goles_total = 0
        goles_total += fecha[opcion_l['equipo']]['goles']
        goles_total += fecha[opcion_v['equipo']]['goles']
        total_fechas = len(lstFechas)

        if total_fechas == 0:
            promedio_goles = 0
        else:
            promedio_goles = goles_total / total_fechas
        
        reportes['totalG']['valor'] = goles_total
        reportes['promedioG']['valor'] = promedio_goles
    
    