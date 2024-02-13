import json 
#Funcion para ingresar campers
def registroCampers():
    ListaCampers=[]    
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
            break
        except ValueError:
            print("Por favor ingrese los valores indicados correctamente\n")
    ListaCampers.append({'nombre': nombre, 'apellidos': apellidos, 'documento':documento,'direccion': direccion, 'Acudiente': Acudiente, 'Telefono': Telefono, 'Estado':Estado, 'Riesgo':Riesgo})
    #Leer al Json
    try:   
        with open('campers.json','r') as Campers:
            data = json.load(Campers)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = []
                
    #Añadir los datos a la lista existente
    data.extend(ListaCampers)
    
    #Escribir al Json
    with open('campers.json','w') as archivo:
        json.dump(data,archivo, indent=4)
    
    
    
registroCampers()        
