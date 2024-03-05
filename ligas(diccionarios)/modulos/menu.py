import os

def CrearMenu():
    lstOpciones = [1,2,3,4,5,6]
    titulo = """
        ++++++++++++++++++++++++++++
        +   LIGA BETPLAY MENU      +
        ++++++++++++++++++++++++++++
    """
    os.system('cls')
    print(titulo)
    try:
        opciones = "1. Agregar equipo\n2. Borrar equipo\n3. Registrar fecha\n4. Tabla de equipos\n5. Reportes\n6. Salir"
        print(opciones)
        op =int(input(':) '))
        if (op not in lstOpciones):
            CrearMenu()
    except ValueError:
        print('Dato invalido')
        os.system('pause')
        CrearMenu()
    else:
        return op


    