import modulos.menu as mp
import modulos.menuReportes as mr
import modulos.equipos as e
import modulos.fechas as fe
if __name__ == '__main__':
    equiposLiga = {}
    Fechas = {
        '1': {},
        '2': {},
        '3': {},
        '4': {},
        '5': {},
        '6': {},
        '7': {},
        '8': {},
        '9': {},
        '10': {},
        '11': {},
        '12': {}
    }
    reportes = {
    'MaxGoles': {'nombre': '', 'valor': 0},
    'MaxPT': {'nombre': '', 'valor': 0},
    'MaxPG': {'nombre': '', 'valor': 0},
    'totalG': {'valor': 0},
    'promedioG': {'valor': 0}
}
    opcion_l = {} 
    opcion_v = {}
    isAppRunning = True
    while isAppRunning:
        op=mp.CrearMenu()
        if (op ==1):
            isAddTeam = True
            while isAddTeam:
                e.os.system('cls')
                e.AddTeam(equiposLiga)
                isAddTeam = bool(input('Desea agregar otro Equipo S(Si) o Enter(No)'))
        elif (op ==2):
            DelTeam = True
            while DelTeam:
                e.os.system('cls')
                e.DelTeam(equiposLiga)
                DelTeam= bool(input('desea eliminar otro equipo? S(Si) ENTER(No)'))
        elif (op ==3):
            AddDate = True
            while AddDate:
                e.os.system('cls')
                fe.Addgame(equiposLiga, Fechas, opcion_l, opcion_v, reportes)
                AddDate = bool(input('Desea agregar otra fecha S(Si) o Enter(No)'))
        elif (op ==4):
            e.ViewTeam(equiposLiga) 
        elif (op ==5):
             isReport = True
             while isReport:
                 opr = mr.CrearMenu()
                 if (opr == 'A'):
                     print(f'el equipo con mas goles es {reportes["MaxGoles"]["nombre"]} con un total de {reportes["MaxGoles"]["valor"]}')
                     e.os.system('pause')
                 elif (opr == 'B'):
                     print(f'el equipo con mas puntos es {reportes["MaxPT"]["nombre"]} con un total de {reportes["MaxPT"]["valor"]}')
                     e.os.system('pause')
                 elif (opr == 'C'):
                     print(f'el equipo con mas goles es {reportes["MaxPG"]["nombre"]} con un total de {reportes["MaxPG"]["valor"]}')
                     e.os.system('pause')
                 elif (opr == 'D'):
                     print(f'el total de goles fue {reportes["totalG"]["valor"]}') 
                     e.os.system('pause')
                 elif (opr == 'E'):
                     print(f'el promedio de goles fue {reportes["promedioG"]["valor"]}') 
                     e.os.system('pause')
                 elif (opr == 'F'):
                     isReport = False
        elif (op ==6):
            isAppRunning=False 