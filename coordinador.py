import json
import jsonsfunciones

#Ingresa la nota teorica y practica de la primera prueba 
def primeraprueba():
    listaEstudiantes=jsonsfunciones.CargarDatos("campers.json")
    print("Selecciona el estudiante al cual le quieres asignar una nota")
    print("---------LISTA DE ESTUDIANTES_______\n")
    for index,camper in enumerate(listaEstudiantes):
        nombre=camper.get('nombre','No hay nombre')
        apellido=camper.get('apellidos','No hay apellidos')
        if camper['Estado'] == "En proceso de ingreso" :
            print(f"{index+1}-{nombre}{apellido}")
    try:
        estudiante=int(input("¿A cual estudiante cambiarás su nota? inserta el numero del estudiante\n"))
        while True:
            notateorica=int(input("Por favor ingresa la nota teorica (#/100)\n"))
            if notateorica<0 or notateorica>100:
                print("Por favor inserta un valor que corresponda al rango de 0 a 100")
            else:
                break
        while True:
            notapractica=int(input("Por favor ingresa la nota practica (#/100)\n"))
            if notapractica<0 or notapractica>100:
                print("Por favor inserta un valor que corresponda al rango de 0 a 100")
            else:
                break    
        notaingreso=(notateorica+notapractica)/2
        print("la nota de ingreso es", notaingreso)
        if notaingreso>60:
            listaEstudiantes[estudiante-1]['Estado']="Aprobado"
            print("Estudiante aprobado")
            jsonsfunciones.guardarcambios(listaEstudiantes,"campers.json")
        if notaingreso<60:
            listaEstudiantes[estudiante-1]['Estado']="Inscrito"
            print("Estudiante no ha aprobado, su estado actual es inscrito")
            jsonsfunciones.guardarcambios(listaEstudiantes,"campers.json")
    except Exception:
        print("El dato ingresado no corresponde a un numero entero\npor favor intentalo de nuevo ")

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

def registroTrainer():
    listaTrainers=jsonsfunciones.CargarDatos("trainer.json")
    while True:
        try:
            nombre=input("Escribe el nombre completo del nuevo trainer\n")
            listaTrainers.append({'nombre': nombre})
            jsonsfunciones.guardarcambios(listaTrainers,"trainer.json")
            print("Trainer creado con exito")
            break
        except ValueError:
            print("Por favor ingrese los valores indicados correctamente\n")    

def asignarruta():
    listaSalones=jsonsfunciones.CargarDatos("salones.json")
    listaTrainer=jsonsfunciones.CargarDatos('trainer.json')
    listaRutas=jsonsfunciones.CargarDatos("rutasaprendizaje.json")        
    try:
        while True:
            print("Los salones sin ruta son")
            print("\n---------LISTA DE SALONES----------\n")
            for index,salon in enumerate(listaSalones):
                rutasalon=listaSalones.get(salon)
                if rutasalon['ruta']=="":
                    print(f"{index+1}-->{salon}")
            salonopcion=int(input("Selecciona el salon al cual le quieres asignar un ruta:  "))
                    
            print("Las rutas disponibles para este salon son ")
            print("\n---------LISTA DE RUTAS----------\n")
            for index,ruta in enumerate(listaRutas):
                print(f"{index+1}-->{ruta.get('Nombre')}")
            rutaelegida=int(input("Elige la ruta que deseas ingresar en el salón:   "))
            
            print("Los Trainers disponibles para este salon son")
            print("\n---------LISTA DE TRAINERS----------\n")
            for index,trainer in enumerate(listaTrainer):
                print(f"{index+1}","-->",trainer.get('nombre'))
            trainerelegido=int(input("Elige el trainer que deseas asignar a este salón:   "))
            
            #Para obtener el nombre del salon
            nombresalon=list(listaSalones.keys())[salonopcion-1]
            
            #Para obtner el horario del salón seleccionado
            horariosalonseleccionado=listaSalones[nombresalon].get('Horario')
            
            #revisar si el trainer está en el mismo horario en otro salón
            fechainicio=input("¿Cuando inicia el curso? \n(DD/MM/AAAA)\n")
            fechafin=input("¿Cuando finaliza el curso? \n(DD/MM/AAAA)\n")
            
            for salon , datosSalon in listaSalones.items():
                if datosSalon['Trainer']==listaTrainer[trainerelegido-1]['nombre'] and datosSalon.get('Horario')==horariosalonseleccionado:
                    print("El Trainer ya se encuentra asignado en un salon con el mismo horario")
                else:
                    #Para asignar los datos al diccionario del salón
                    datosSalon=listaSalones.get(nombresalon,{})
                    datosSalon['Trainer']=listaTrainer[trainerelegido-1]['nombre']
                    datosSalon['ruta'] = listaRutas[rutaelegida - 1]['Nombre']
                    datosSalon['fechainicio'] = fechainicio
                    datosSalon['Fechafin'] = fechafin
                    listaSalones[nombresalon] = datosSalon
                    jsonsfunciones.guardarcambios(listaSalones,"salones.json")
                break
            break
    except KeyboardInterrupt:
        print("Proceso interrumpido.")
        

def asignarsalon():
    listaEstudiantes=jsonsfunciones.CargarDatos("campers.json")
    listaSalones=jsonsfunciones.CargarDatos("salones.json")
    print("\n")
    print("Solo puedes asignar salon a los estudiantes que hayan presentado prueba de ingreso\n y hayan aprobado el examen. ")
    print("Los estudiantes que superaron la prueba de ingreso son")
    print("---------LISTA DE ESTUDIANTES----------\n")
    for index,camper in enumerate(listaEstudiantes):
        nombre=camper.get('nombre','No hay nombre')
        apellido=camper.get('apellidos','No hay apellidos')
        if camper['Estado'] == "Aprobado" and camper['Salon']=="":
            print(f"{index+1}-{nombre}{apellido}")
    while True:
        try:
            estudiante=int(input("¿A cual estudiante deseas asignar un area? inserta el numero del estudiante:   "))
            print("\nLos salones con una ruta son")
            print("\n---------LISTA DE SALONES CON RUTA DEFINIDA----------\n")
            for index,salon in enumerate(listaSalones):
                rutasalon=listaSalones.get(salon)
                if rutasalon['ruta']!="" and rutasalon['Ocupacion']<33:
                    print(f"{index+1}-->{salon} y la ruta del salon es {rutasalon['ruta']}")
            salonopcion=int(input("Selecciona el salon al cual quieres inscribir al estudiante: "))
            nombresalon=list(listaSalones.keys())[salonopcion-1]  
            listaEstudiantes[estudiante-1]["Salon"]=nombresalon
            listaEstudiantes[estudiante-1]["datosSalon"]=listaSalones[nombresalon]
            #determinar la ocupación del salón 
            ocupacion = sum(1 for camper in listaEstudiantes if camper.get('Salon')==nombresalon)
            #asignar la ocupación al salón
            listaSalones[nombresalon]['Ocupacion']= ocupacion
            #Se cambia el estado a cursando ya que se encuentran inscritos en una ruta y un salón
            listaEstudiantes[estudiante-1]["Estado"]="Cursando"
            #es necesario guardar los dos jsons pilas!
            jsonsfunciones.guardarcambios(listaEstudiantes,"campers.json")     
            jsonsfunciones.guardarcambios(listaSalones,"salones.json")
            break
        except Exception:
           print("Proceso interrumpido, ingresa una de las opciones mostradas")
        
               
def notamodulo():
    listaEstudiantes=jsonsfunciones.CargarDatos("campers.json")
    for index,camper in enumerate(listaEstudiantes):
        nombre=camper.get('nombre','No hay nombre')
        apellido=camper.get('apellidos','No hay apellidos')
        if camper['Estado'] == "Cursando" :
            print(f"{index+1}-{nombre}{apellido}")
    opcionestudiante=int(input("Elige el numero del estudiante al cual le asignaras una calificación:  "))
    
    print("Para asignar la nota del modulo necesitamos")
    notafinalmodulo()
    
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
            notasEstudianteSelec[x]=notafinalmodulo
            print("La nota fue asignada exitosamente en el modulo:  ", x)
            break
    
    jsonsfunciones.guardarcambios(listaEstudiantes,"campers.json")
            
    
 
notamodulo()