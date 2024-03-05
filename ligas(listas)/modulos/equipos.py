def AddTeam(Equipos: list):
    Nombre= str(input('ingrese el nombre del equipo que quiere añadir: '))
    Equipos.append([Nombre, 0, 0, 0, 0, 0, 0])
    return Nombre