  

def crear_menu():

    op = [1, 2, 3, 4]

    titulo = """
    ++++++++++++++++++++++++++++++
    + LIGA BETPLAY COLOMBIA 2024 +
    ++++++++++++++++++++++++++++++
    """
    print(titulo)
    
    
    menu = str('1. Registrar equipo\n2. Registrar fecha de juego\n3. Reportes\n4. Salir')
    print(menu)

    try:
        opcion = int(input('ingrese una opcion'))
        if not(opcion in op):
            print('ingrese una opcion valida')
            crear_menu()
    except ValueError:
        print('ingrese una opcion valida')
        crear_menu()
    else:
        return opcion
    
    