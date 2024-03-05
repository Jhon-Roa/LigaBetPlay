def MenuReportes():
    
    
    titulo = """
    +++++++++++++++++++++++
    + REPORTES DEL TORNEO +
    +++++++++++++++++++++++
    """
    print(titulo)
    
    Menu = ['A. Nombre del equipo que mas goles anoto','B. Nombre del equipo que mas puntos tiene','C. Nombre del equipo que mas partidos gano','D. Total de goles anotados por todos los equipos','E. Promedio de goles anotados en el torneo','F. Salir']
    for item in Menu:
        print(item)
    
    try:
        op = str(input('ingrese la opcion a elegir')).upper()
    except:
        print('ingrese un valor valido')
        MenuReportes()
    else:
        return op
    
