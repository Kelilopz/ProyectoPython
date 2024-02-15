import json 
import jsonsfunciones
#Crear un nuevo tema

def CrearTema():
    listaTemas=jsonsfunciones.CargarDatos("rutas.json")
    try:
        while True:
            opcion=int(input("Que deseas cambiar?\n1.)Fundamentos de programacion\n2.)Programacion web\n3.)Programacion formal\n4.)SGBD(Bases de datos)\n5.)Backend\n0.)Para salir\n"))
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
    try:
        nombreruta = input("Por favor escribe el nombre de la nueva ruta\n")
        while True:
            print("Los temas que todas las rutas deben ver son los siguientes\n")
            print("Fundamentos de programación", listaTemas['fundamentosProgramacion'])
            print("Programación Web", listaTemas['Programacionweb'])
            print("Programación Formal", listaTemas['ProgramacionFormal'])
            print("Elige un SGDB de los que se encuentran a continuación")
            for x in listaTemas['SGBD']:  # Aquí se corrige 'SGDB' a 'SGBD'
                print(x)
            break 
    except Exception:
        print("Los datos ingresados no corresponden a un número")

CrearRuta()