import json 
#Escribir al Json                
def guardarcambios(rutas):
    with open('rutas.json','w') as archivo:
        escritura = json.dumps(rutas)
        archivo.write(escritura)
    

#Leer al Json
def CargarDatos(): 
    try:   
        with open('rutas.json','r') as RutasNew:
            Rutas = json.load(RutasNew)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        Rutas = []
    return Rutas


#Crear un nuevo tema

def CrearTema():
    listaTemas=CargarDatos()
    try:
        opcion=int(input("Que deseas cambiar?\n1.)Obligatorios\n2.)SGBD(Bases de datos)\n3.)Backend\n"))
        while True:
            if opcion==1:
                obligatorios=input("Escribe tus obligatorios\n")
                listaTemas.append({'obligatorios': obligatorios})
                guardarcambios(listaTemas)
                print("Tema creado con exito")
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
                guardarcambios(listaTemas)
                print("Tema creado con exito")
                break
            else:
                print("No elegiste una opción correcta, intentalo de nuevo")
    except exception:
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