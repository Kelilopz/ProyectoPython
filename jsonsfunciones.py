import json
import os

#Escribir al Json                
def guardarcambios(datos,archivo):
    with open(archivo,'w') as archivonew:
        escritura = json.dumps(datos , indent = 4)
        archivonew.write(escritura)
        print("Tus datos han sido guardados EXITOSAMENTE")
    

#Leer al Json
def CargarDatos(archivo): 
    try:   
        with open(archivo,'r') as file:
            respuesta = json.load(file)
            return respuesta
    except Exception:
        return []
    
def limpiarTerminal():
    # Verifica si el sistema operativo es Windows
    if os.name == 'nt':
        _ = os.system('cls')  # Limpia la terminal en Windows
    else:
        _ = os.system('clear')  # Limpia la terminal en sistemas Unix (Linux, macOS)
