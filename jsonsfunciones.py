#Escribir al Json                
def guardarcambios(datos,archivo):
    with open('rutas.json','w') as archivo:
        escritura = json.dumps(datos,ident=4)
        archivo.write(escritura)
    

#Leer al Json
def CargarDatos(archivo): 
    try:   
        with open(archivo,'r') as file:
            respuesta = json.load(file)
            return respuesta
    except Exception:
        return []