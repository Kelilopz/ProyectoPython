import json 
import jsonsfunciones
#Crear un nuevo tema

def CrearTema():
    listaTemas=jsonsfunciones.CargarDatos("rutas.json")
    try:
        while True:
            opcion=int(input("Que deseas añadir?\n1.)Fundamentos de programacion\n2.)Programacion web\n3.)Programacion formal\n4.)SGBD(Bases de datos)\n5.)Backend\n0.)Para salir\n"))
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
        