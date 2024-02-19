import json
import jsonsfunciones

#Funcion para ingresar campers

def registroCampers():
    ListaCampers=jsonsfunciones.CargarDatos("campers.json")
    print("--------------------------------")
    print("-------Registro de Camper-------")
    print("--------------------------------") 
    while True:
        try:
            nombre=input("Escribe solo tus nombres\n")
            apellidos=input("Escribe tus apellidos\n")
            documento=int(input("Por favor escribe tu documento de identidad\n"))
            direccion=input("Escribe tu dirección de residencia\n") 
            Acudiente=input("Escribe el nombre de tu acudiente\n")
            Telefono=int(input("Escribe tu numero de celular\n")) 
            Estado="En proceso de ingreso"
            Riesgo=""
            Salon=""
            DatosSalon=""
            Notas={
                'Fundamentos de Programacion':None,
                'Programacion Web':None,
                'Programacion Formal':None,
                'SGBD':None,
                'Backend':None
            }
            ListaCampers.append({'nombre': nombre, 'apellidos': apellidos, 'documento':documento,'direccion': direccion, 'Acudiente': Acudiente, 'Telefono': Telefono, 'Estado':Estado, 'Riesgo':Riesgo,'Salon':Salon,'datosSalon':DatosSalon,'Notas':Notas})
            jsonsfunciones.guardarcambios(ListaCampers,"campers.json")
            print("Usuario creado con exito")
            break
        except ValueError:
            print("Por favor ingrese los valores indicados correctamente\n")    

def campersInscritos():
    listaEstudiantes=jsonsfunciones.CargarDatos("campers.json")
    print("----------------------------------------")
    print("-------Lista de Campers Inscritos-------")
    print("----------------------------------------") 
    for index,camper in enumerate(listaEstudiantes):
        nombre=camper.get('nombre','No hay nombre')
        apellido=camper.get('apellidos','No hay apellidos')
        if camper['Estado'] == "En proceso de ingreso" or camper['Estado'] == "Inscrito" :
            print(f"{index+1}-{nombre}{apellido}")
            
def campersAprobados():
    listaEstudiantes=jsonsfunciones.CargarDatos("campers.json")
    print("----------------------------------------")
    print("-------Lista de Campers Aprobados-------")
    print("----------------------------------------") 
    for index,camper in enumerate(listaEstudiantes):
        nombre=camper.get('nombre','No hay nombre')
        apellido=camper.get('apellidos','No hay apellidos')
        if camper['Estado'] == "Aprobado" or camper['Estado'] == "Cursando" :
            print(f"{index+1}-{nombre}{apellido}")

def trainersInCampus():
    listaSalones = jsonsfunciones.CargarDatos("salones.json")
    listaprofes = set()
    print("----------------------------------------------------")
    print("-------Lista de Trainers Trabajando en Campus-------")
    print("----------------------------------------------------") 
    for salon in listaSalones.values():
        profeasignado = salon.get('Trainer','Sin Trainer')
        if profeasignado != "":
            if profeasignado not in listaprofes:
                listaprofes.add(profeasignado)
    cont = 0
    for x in listaprofes:
        cont += 1
        print(f"{cont}--> {x}")

def campersRendimientoBajo():
    listaEstudiantes=jsonsfunciones.CargarDatos("campers.json")
    print("---------------------------------------------------")
    print("-------Lista de Campers Con Rendimiento BAJO-------")
    print("---------------------------------------------------") 
    for index,camper in enumerate(listaEstudiantes):
        nombre=camper.get('nombre','No hay nombre')
        apellido=camper.get('apellidos','No hay apellidos')
        if camper['Riesgo'] == "Alto" :
            print(f"{index+1}-{nombre}{apellido}")

def campersYtrainersEnUnaRuta():
    listaEstudiantes=jsonsfunciones.CargarDatos("campers.json")
    listaRutas=jsonsfunciones.CargarDatos('rutasaprendizaje.json')
    listaSalones=jsonsfunciones.CargarDatos('salones.json')
    listaprofes=set()
    print("---------------------------------------------------")
    print("-------Lista de Campers y Trainers la Ruta --------")
    print("---------------------------------------------------") 
    
    
    while True:
        #Definir cual ruta vamos a revisar
        print("\nLas Rutas disponibles son:\n")
        for index,ruta in enumerate(listaRutas):
            nombre=ruta.get('Nombre','No hay nombre')
            if nombre!="":
                print(f"{index+1}-{nombre}")
        try:
            rutaseleccionada=int(input("\nLa ruta que deseas revisar es:  "))
            if rutaseleccionada<0 or rutaseleccionada>index+1:
                print("Este valor no corresponde a las opciones")
            else:
                while True:
                    hacer=int(input("¿Que deseas revisar?\n1. Campers\n2. Trainers\n0. Volver al menú anterior\nOpción:   "))
                    nombreruta=listaRutas[rutaseleccionada-1]['Nombre']
                    if hacer==1:
                        #Entontrar el nombre de la ruta seleccionada
                        print("--------------------------------------------------------")
                        print(f"Para la {nombreruta} los ESTUDIANTES asignados son")
                        print("--------------------------------------------------------")
                        for index,camper in enumerate(listaEstudiantes):
                            nombre=camper.get('nombre','No hay nombre')
                            apellido=camper.get('apellidos','No hay apellidos')
                            if camper['datosSalon']['ruta']== nombreruta :
                                print(f"{index+1}-{nombre} {apellido}")
                    elif hacer==2:        
                         # Encontrar los trainers asignados a la ruta seleccionada
                        print("--------------------------------------------------------")
                        print(f"Para la {nombreruta} los TRAINERS asignados son")
                        print("--------------------------------------------------------")
                        for salon in listaSalones:
                            datosSalon = listaSalones[salon]
                            if datosSalon.get('ruta') == nombreruta:
                                profeRuta = datosSalon.get('Trainer')
                                if profeRuta not in listaprofes:
                                    listaprofes.add(profeRuta)                         
                        cont = 0
                        for x in listaprofes:
                            cont += 1
                            print(f"{cont}--> {x}")
                        print("\n")
                    elif hacer == 0:
                        print("....Saliendo....")
                        break
                    else: 
                        print("La opción no es valida, intentalo de nuevo")
        except Exception:
            print("\nVuelve a intentarlo\n")            
    
    
def camperspormodulo():
    listaEstudiantes = jsonsfunciones.CargarDatos("campers.json")
    listaSalones = jsonsfunciones.CargarDatos("salones.json")
    resultados = {}

    
    for camper in listaEstudiantes:
        nombre=camper.get('nombre','No hay nombre')
        apellido=camper.get('apellidos','No hay apellidos')
        ruta=camper['datosSalon']['ruta']
        trainerencargado=camper['datosSalon']['Trainer']
            

        if ruta and trainerencargado:
            resultados.setdefault(ruta, {})
            resultados[ruta].setdefault(trainerencargado, {'Aprobados': 0, 'Perdidos': 0})

            # Supongamos que tienes un campo en el JSON que indica si el camper aprobó o no el módulo
            aprobado = camper.get('aprobado', False)

            if aprobado:
                resultados[ruta][trainerencargado]['Aprobados'] += 1
            else:
                resultados[ruta][trainerencargado]['Perdidos'] += 1

    # Mostrar los resultados
    print("Resultados de los campers por módulo, ruta y entrenador:")
    for ruta, entrenadores in resultados.items():
        print(f"Ruta de entrenamiento: {ruta}")
        for entrenador, datos in entrenadores.items():
            print(f"  Entrenador: {entrenador}")
            print(f"    Campers aprobados: {datos['Aprobados']}")
            print(f"    Campers perdidos: {datos['Perdidos']}")
        print()

# Llamar a la función para obtener y mostrar los resultados
camperspormodulo()