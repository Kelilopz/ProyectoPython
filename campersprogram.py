import json
import jsonsfunciones

#Funcion para ingresar campers

def registroCampers():
    ListaCampers=jsonsfunciones.CargarDatos("campers.json")
    while True:
        try:
            nombre=input("Escribe solo tus nombres\n")
            apellidos=input("Escribe tus apellidos\n")
            documento=int(input("Por favor escribe tu documento de identidad\n"))
            direccion=input("Escribe tu dirección de residencia\n") 
            Acudiente=input("Escribe el nombre de tu acudiente\n")
            Telefono=int(input("Escribe tu numero de celular\n")) 
            Estado="En proceso de ingreso"
            Riesgo=""
            Salon=""
            DatosSalon=""
            Notas=[None,None,None,None,None]
            ListaCampers.append({'nombre': nombre, 'apellidos': apellidos, 'documento':documento,'direccion': direccion, 'Acudiente': Acudiente, 'Telefono': Telefono, 'Estado':Estado, 'Riesgo':Riesgo,'Salon':Salon,'datosSalon':DatosSalon,'Notas':Notas})
            jsonsfunciones.guardarcambios(ListaCampers,"campers.json")
            print("Usuario creado con exito")
            break
        except ValueError:
            print("Por favor ingrese los valores indicados correctamente\n")    

registroCampers()