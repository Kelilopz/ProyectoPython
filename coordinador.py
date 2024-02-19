import json
import jsonsfunciones

#Ingresa la nota teorica y practica de la primera prueba 
def primeraprueba():
    listaEstudiantes=jsonsfunciones.CargarDatos("campers.json")
    
    print("-----------------------------------------")
    print("-------Asignar Nota Prueba Ingreso-------")
    print("-----------------------------------------") 
    
    print("\nSelecciona el estudiante al cual le quieres asignar una nota")
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

#Registar el nombre de un TRainer
def registroTrainer():
    listaTrainers=jsonsfunciones.CargarDatos("trainer.json")
    print("-----------------------------------------")
    print("--------Registro de Nuevo Trainer--------")
    print("-----------------------------------------") 
    
    while True:
        try:
            nombre=input("Escribe el nombre completo del nuevo trainer\n")
            listaTrainers.append({'nombre': nombre})
            jsonsfunciones.guardarcambios(listaTrainers,"trainer.json")
            print("Trainer creado con exito")
            break
        except ValueError:
            print("Por favor ingrese los valores indicados correctamente\n")    

#Asignar una ruta al salón

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

#Asignar un salón a los estudiantes y sus atributos        
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


#Crear un nuevo tema

def CrearTema():
    listaTemas=jsonsfunciones.CargarDatos("rutas.json")
    print("-------------------------------------")
    print("-------Crear Un Tema Para Ruta-------")
    print("-------------------------------------")
    try:
        while True:
            opcion=int(input("Que deseas añadir?\n1.)Fundamentos de programacion\n2.)Programacion web\n3.)Programacion formal\n4.)SGBD(Bases de datos)\n5.)Backend\n0.)Para salir\n\nOpcion:   "))
            if opcion==1:
                Fundamentos_de_programacion=input("Escribe el nuevo fundamento\n")
                if any(Fundamentos_de_programacion == x for x in listaTemas['fundamentosProgramacion']):
                    print("El tema ya se encuentra registrado")
                else:
                    listaTemas['fundamentosProgramacion'].append(Fundamentos_de_programacion)
                    jsonsfunciones.guardarcambios(listaTemas, "rutas.json")
                    print("Tema añadido con Éxito ")
                    print(listaTemas)    
            elif opcion == 2:
                ProgramacionWeb = input("Escribe el nuevo tema de programación Web\n")
                if any(ProgramacionWeb == x for x in listaTemas['Programacionweb']):
                    print("El tema ya se encuentra registrado")
                else:
                    listaTemas['Programacionweb'].append(ProgramacionWeb)
                    jsonsfunciones.guardarcambios(listaTemas, "rutas.json")
                    print("Tema añadido con Éxito ")
                    print(listaTemas)
            elif opcion == 3:
                ProgramacionFormal = input("Escribe el nuevo tema de programación Formal\n")
                if any(ProgramacionFormal == x for x in listaTemas['ProgramacionFormal']):
                    print("El tema ya se encuentra registrado")
                else:
                    listaTemas['ProgramacionFormal'].append(ProgramacionFormal)
                    jsonsfunciones.guardarcambios(listaTemas, "rutas.json")
                    print("Tema añadido con Éxito ")
                    print(listaTemas)
            elif opcion == 4:
                SGBD = input("Escribe el nuevo tus SGBD\n")
                if any(SGBD == x for x in listaTemas['SGBD']):
                    print("El tema ya se encuentra registrado")
                else:
                    listaTemas['SGBD'].append(SGBD)
                    jsonsfunciones.guardarcambios(listaTemas, "rutas.json")
                    print("Tema añadido con Éxito ")
                    print(listaTemas)
            elif opcion == 5:
                Backend = input("Escribe tus Backend\n")
                if any(Backend == x for x in listaTemas['Backend']):
                    print("El tema ya se encuentra registrado")
                else:
                    listaTemas['Backend'].append(Backend)
                    jsonsfunciones.guardarcambios(listaTemas, "rutas.json")
                    print("Tema añadido con Éxito ")
                    print(listaTemas)
            elif opcion == 0:
                break
            else:
                print("No elegiste una opción correcta, inténtalo de nuevo")
    except Exception:
        print("No escribiste un valor numérico, inténtalo de nuevo")
           
#Crear una nueva ruta
def CrearRuta():
    lista_rutas = jsonsfunciones.CargarDatos("rutasaprendizaje.json")
    listaTemas = jsonsfunciones.CargarDatos("rutas.json")

    print("-------------------------------------")
    print("--------Crear una nueva Ruta---------")
    print("-------------------------------------")
    while True:
        
        Fundamentos=listaTemas['fundamentosProgramacion']
        ProgramacionWeb=listaTemas['Programacionweb']
        ProgramacionFormal=listaTemas['ProgramacionFormal']
        SGBD=[]
        Backend=[]
        try:
            nombreruta = input("Por favor escribe el nombre de la nueva ruta\n")
            print("Los temas que todas las rutas deben ver son los siguientes\n")
            print("Fundamentos de programación = ", listaTemas['fundamentosProgramacion'])
            print("Programación Web            = ", listaTemas['Programacionweb'])
            print("Programación Formal         = ", listaTemas['ProgramacionFormal'])
            print("Elige un SGDB de los que se encuentran a continuación\n")
            cont=0
            for x in listaTemas['SGBD']:  
                print(cont," -> ",x)
                cont+=1
                     
            while True:    
                sgbdprincipal=int(input("inserta el numero del SBDB que deseas elegir como PRINCIPAL\n"))
                if sgbdprincipal < 0 or sgbdprincipal >= cont:
                    print("Por favor, elige un número válido dentro del rango.")
                else:
                    SGBD.append(listaTemas['SGBD'][sgbdprincipal])
                    break
                
            while True:
                sgbdsecundario = int(input("Inserta el número del SSDB que deseas elegir como SECUNDARIO\n"))
                if sgbdsecundario < 0 or sgbdsecundario >= cont:
                    print("Por favor, elige un número válido dentro del rango.")
                elif sgbdprincipal == sgbdsecundario:
                    print("No puedes elegir el mismo valor para los dos sgbd.")
                else:
                    SGBD.append(listaTemas['SGBD'][sgbdsecundario])
                    break
            
            print("Elige un valor para el backend de los que se presentan a continuación\n")            
            contador=0
            for x in listaTemas['Backend']:  
                print(contador," -> ",x) 
                contador+=1
            
            while True:
                backend=int(input("Inserta el numero del backend que deseas elegir\n"))
                if backend < 0 or backend >= contador:
                    print("Por favor, elige un número válido dentro del rango.")
                else:
                    Backend.append(listaTemas['Backend'][backend])
                break
            lista_rutas.append({'Nombre':nombreruta,'Fundamentos':Fundamentos,'ProgramacionWeb':ProgramacionWeb,'ProgramacionFormal':ProgramacionFormal,'SGBD':SGBD,'Backend':Backend}) 
            jsonsfunciones.guardarcambios(lista_rutas,"rutasaprendizaje.json")
            print(lista_rutas)
            break            
        except Exception:
            print("Los datos ingresados no corresponden a un número")
                