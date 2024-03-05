import modulos.menu as mp
import modulos.reportes as mr
import modulos.equipos as eq
import modulos.fechas as fe

if __name__ == "__main__":
    IssAppRunning = True
    Equipos= []
    while IssAppRunning:
        op = mp.crear_menu()
        if op == 1:
            AddEquipo = True
            while AddEquipo:
                Nombre = eq.AddTeam(Equipos)
                AddEquipo= bool(input('Desea ingresar otro equipo, s[SI] o Enter[No]'))
        elif op == 2:
            AddDate= True
            while AddDate:
                local = str(input('ingrese el equipo que debuto de local: '))
                visitante =  str(input('ingrese el equipo que debuto de visitante: '))
                fe.fecha(local, visitante)
        elif op == 3:
            IsReport = True
            while IsReport:
                op = mr.MenuReportes()
                if op == 'A':
                    pass
                elif op == 'B':
                    pass
                elif op == 'C':
                    pass
                elif op == 'D':
                    pass
                elif op == 'E':
                    pass
                elif op == 'F':
                    IsReport = False
        elif op == 4:
            break