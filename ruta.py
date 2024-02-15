import json 
import jsonsfunciones
#Crear un nuevo tema

def CrearTema():
    listaTemas=jsonsfunciones.CargarDatos("rutas.json")
    try:
        opcion=int(input("Que deseas cambiar?\n1.)Fundamentos de programacion\n2.)Programacion web\n3.)Programacion formal\n4.)SGBD(Bases de datos)\n5.)Backend\n0.)Para salir\n"))
        while True:
            if opcion==1:
                Fundamentos_de_programacion=input("Escribe el nuevo fundamento\n")
                for x in listaTemas['fundamentosProgramacion']:
                    if Fundamentos_de_programacion.lower==x:
                        print("El tema ya se encuentra registrado")
                        break
                    else:
                        listaTemas['fundamentosProgramacion'].append(Fundamentos_de_programacion)
                        jsonsfunciones.guardarcambios(listaTemas,"rutas.json")
                        print("Tema añadido con Exito ")
                        print (listaTemas)
                        break
            elif opcion==2:
                ProgramacionWeb=input("Escribe el nuevo tema de programación Web\n")
                listaTemas['Programacionweb'].append(ProgramacionWeb)
                jsonsfunciones.guardarcambios(listaTemas,"rutas.json")
                print("Tema añadido con Exito ")
                print (listaTemas)
                break
                
            elif opcion==3:
                ProgramacionFormal=input("Escribe el nuevo tema de programación Formal\n")
                listaTemas['ProgramacionFormal'].append(ProgramacionFormal)
                jsonsfunciones.guardarcambios(listaTemas,"rutas.json")
                print("Tema añadido con Exito ")
                print (listaTemas)
                break
            elif opcion==4:
                SGBD=input("Escribe el nuevo tus SGBD\n")
                listaTemas['SGBD'].append(SGBD)
                jsonsfunciones.guardarcambios(listaTemas,"rutas.json")
                print("Tema añadido con Exito ")
                print (listaTemas)
                break
            elif opcion==5:
                Backend=input("Escribe tus Backend\n")
                listaTemas['Backend'].append(Backend)
                jsonsfunciones.guardarcambios(listaTemas,"rutas.json")
                
                print (listaTemas)
                break
            elif opcion==0:
                break
            else:
                print("No elegiste una opción correcta, intentalo de nuevo")
    except Exception:
        print("No escribiste un valor numerico intentalo de nuevo")

#Crear una nueva ruta
#def CrearRuta():
#    lista_rutas=jsonsfunciones.CargarDatos()
#    nombreruta=input("Por favor escribe el nomobre de la nueva ruta")
    
#    while True:
#       try:
#           SGDB_principal=(int(input(
#               "Por favor elige la Base de datos que deseas seleccionar principal"
#                                     lista_SGBD)))
            
CrearTema()