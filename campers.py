import json 
#Escribir al Json                
def guardarcambios(datos):
    with open('campers.json','w') as archivo:
        escritura = json.dumps(datos)
        archivo.write(escritura)
    

#Leer al Json
def CargarDatos(): 
    try:   
        with open('campers.json','r') as Campers:
            data = json.load(Campers)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = []
    return data

#Funcion para ingresar campers

def registroCampers():
    ListaCampers=list(CargarDatos())   
    while True:
        try:
            nombre=input("Escribe tu solo tus nombres\n")
            apellidos=input("Escribe tus apellidos\n")
            documento=int(input("Por favor escribe tu documento de identidad\n"))
            direccion=input("Escribe tu dirección de residencia\n") 
            Acudiente=input("Escribe el nombre de tu acudiente\n")
            Telefono=int(input("Escribe tu numero de celular\n")) 
            Estado="En proceso de ingreso"
            Riesgo="Bajo"
            Ruta=None
            ListaCampers.append({'nombre': nombre, 'apellidos': apellidos, 'documento':documento,'direccion': direccion, 'Acudiente': Acudiente, 'Telefono': Telefono, 'Estado':Estado, 'Riesgo':Riesgo,'Ruta':Ruta})
            guardarcambios(ListaCampers)
            print("Usuario creado con exito")
            break
        except ValueError:
            print("Por favor ingrese los valores indicados correctamente\n")    

registroCampers()