import json 
import jsonsfunciones
#Crear un nuevo tema

def CrearTema():
    listaTemas=jsonsfunciones.CargarDatos("rutas.json")
    try:
        opcion=int(input("Que deseas cambiar?\n1.Fundamentos de programacion\n2.)Programacion web\n3.)Programacion formal\n4.)SGBD(Bases de datos)\n5.)Backend\n0.)Para salir\n"))
        while True:
            if opcion==1:
                Fundamentos_de_programacion=input("Escribe el nuevo fundamento\n")
                listafundamentos=listaTemas['Fundamentos de programacion']
                listafundamentos.append(Fundamentos_de_programacion)
                jsonsfunciones.guardarcambios(listafundamentos)
                print (listaTemas)
                break
            elif opcion==2:
                SGBD=input("Escribe tus SGBD\n")
                listaTemas.append({'SGBD': SGBD})
                guardarcambios(listaTemas)
                print("Tema creado con exito")
                break
            elif opcion==3:
                Backend=input("Escribe tus Backend\n")
                listaTemas.append({'Backend': Backend})
                guardarcambios(listaTemas,"campers.json")
                print("Tema creado con exito")
                break
            else:
                print("No elegiste una opción correcta, intentalo de nuevo")
    except Exception:
        print("No escribiste un valor numerico intentalo de nuvo")

#Crear una nueva ruta
#def CrearRuta():
#    lista_SGBD=list(CargarDatos())
#    nombreruta=input("Por favor escribe el nomobre de la nueva ruta")
#    
#    while True:
#       try:
#           SGDB_principal=(int(input(
#               "Por favor elige la Base de datos que deseas seleccionar principal"
#                                     lista_SGBD)))
            
CrearTema()