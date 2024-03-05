def fecha(local, visitante):

    GolesL = True
    while GolesL:
        try:
            GolesL = int(input('ingrese los goles del equipo local: '))
        except:
            print('ingrese un valor valido')
        else:
            GolesL = False
            
    GolesV = True
    while GolesV:
        try:
            GolesV = int(input('ingrese los goles del equipo visitante: '))
        except:
            print('ingrese un valor valido')
        else:
            GolesV = False
            
    if GolesL == GolesV:
        print(str(f'el marcador fue {GolesL} - {GolesV}'))
        print(str('fue un empate'))
    elif GolesL > GolesV:
        print(str(f'el marcador fue {GolesL} - {GolesV}'))
        print(str(f'Gano {local}'))
    else:
        print(str(f'el marcador fue {GolesV} - {GolesL}'))
        print(str(f'gano {visitante}'))
        
        
        