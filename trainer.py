import json
import jsonsfunciones



def notafinalmodulo():
    while True:
        try:
            notateorica=int(input("Escribe la nota teorica:   "))
            notapractica=int(input("Escribe la nota practica:  "))
            notaprofe=int(input("Escribe la nota correspondiente a quizes y talleres de clase:  "))
            
            notamodulo=(notateorica*0.3)+(notapractica*0.6)+(notaprofe*0.1)
            print("La nota final de este modulo es --> ",notamodulo)
            return notamodulo
        except Exception:
            print("Por favor escribe un valor que corresponda ")
       
               
def notamodulo():
    print("--------------------------------------")
    print("---------Asignar Nota Modulo----------")
    print("--------------------------------------")
    listaEstudiantes=jsonsfunciones.CargarDatos("campers.json")
    for index,camper in enumerate(listaEstudiantes):
        nombre=camper.get('nombre','No hay nombre')
        apellido=camper.get('apellidos','No hay apellidos')
        if camper['Estado'] == "Cursando" :
            print(f"{index+1}-{nombre}{apellido}")
    opcionestudiante=int(input("Elige el numero del estudiante al cual le asignaras una calificación:  "))
    
    print("Para asignar la nota del modulo necesitamos")
    
    #Para identificar las notas del estudiante que seleccionamos arriba
    notasEstudianteSelec=listaEstudiantes[opcionestudiante-1]['Notas']
    #Para mostrar las notas de los modulos anteriores
    print("\n Modulos anteriores y nota sobtenidas")
    for modulo, nota in notasEstudianteSelec.items():
        if nota is not None:
            print(f"-{modulo}:{nota}")
            
    #Para asignar una nueva nota al los modulos 
 
    for x in notasEstudianteSelec:
        if notasEstudianteSelec[x] is None:
            nuevaNota=notafinalmodulo()
            if nuevaNota<60:
                listaEstudiantes[opcionestudiante-1]['Riesgo']="Alto"
                print("El estudiante REPROBÓ este modulo")
                reporte="Reprobado"
            if nuevaNota>60:
                listaEstudiantes[opcionestudiante-1]['Riesgo']="Bajo"
                print("El estudiante APROBÓ este modulo")
                reporte="Aprobado"
            notasEstudianteSelec[x]=[nuevaNota,reporte]
            
                
            print("La nota fue asignada exitosamente en el modulo:  ", x)
            break
    
    jsonsfunciones.guardarcambios(listaEstudiantes,"campers.json")

