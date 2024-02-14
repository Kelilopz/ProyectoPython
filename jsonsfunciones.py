import json

#Escribir al Json                
def guardarcambios(datos,archivo):
    with open(archivo,'w') as archivonew:
        escritura = json.dumps(datos , indent = 4)
        archivonew.write(escritura)
    

#Leer al Json
def CargarDatos(archivo): 
    try:   
        with open(archivo,'r') as file:
            respuesta = json.load(file)
            return respuesta
    except Exception:
        return []