import os
def CrearMenu():
    lstOpciones = ['A','B', 'C', 'D', 'E','F']
    opciones = ['A. Equipo Goleador','B. Equipo Mas Puntos', 'C. Equipo que mas partidos gano', 'D. Total de Goles', 'E. Promedio de goles', 'F. Salir menu principal']
    os.system('cls')
    titulo = """
        ++++++++++++++++++++++++++++
        +   LIGA BETPLAY REPORTES  +
        ++++++++++++++++++++++++++++
    """
    print(titulo)
    for item in opciones:
        print(item)
    try:
        op = input(':)_').upper()
    except:
        print('Error en la opcion')
        os.system('pause')
        CrearMenu()
    else:
        return op
