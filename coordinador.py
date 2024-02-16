import json
import jsonsfunciones

#Ingresa la nota teorica y practica de la primera prueba 
def primeraprueba():
    listaEstudiantes=jsonsfunciones.CargarDatos("campers.json")
    print("Selecciona el estudiante al cual le quieres asignar una nota")
    print("---------LISTA DE ESTUDIANTES_______\n\n")
    for index,camper in enumerate(listaEstudiantes):
        nombre=camper.get('nombre','No hay nombre')
        apellido=camper.get('apellidos','No hay apellidos')
        if camper['Estado']="En proceso de ingreso":
            print(f"{index+1}-{nombre}{apellido}")
    while True:
        notateorica=int(input("Por favor ingresa la nota teorica (#/100)\n"))
        if notateorica<0 or notateorica>100:
            print("Por favor inserta un valor que corresponda al rango de 0 a 100")
        else:
            break
    while True:
        notapractica=int(input("Por favor ingresa la nota practica (#/100)\n"))
        if notapractica<0 or notapractica>100:
            print("Por favor inserta un valor que corresponda al rango de 0 a 100")
        else:
            break    
    notaingreso=(notateorica+notapractica)/2
    print("la nota de ingreso es", notaingreso)
    if notaingreso>60:
        print("Estudiante aprobado")
        print("se asigna la nota al estudiante")


primeraprueba()