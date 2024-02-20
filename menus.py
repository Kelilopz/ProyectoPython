import json
import campersprogram
import jsonsfunciones
import coordinador
import trainer


def menuCamper():
    while True:
        try:
            jsonsfunciones.limpiarTerminal()
            print("-------------------------------")
            print("-------Bienvenido Camper-------")
            print("-------------------------------") 
            print("Selecciona lo que deseas realizar:")
            print("1. Registrar Camper")
            print("0. Salir al menú anterior")
            opcion = int(input("\n Opción: "))
            if opcion==1:
                jsonsfunciones.limpiarTerminal()
                campersprogram.registroCampers()
            elif opcion==0:
                print("Saliendo...")
                break
            else:
                print("La opción seleccionada no es correcta, intentalo nuevamente ")
        except Exception:
            print("ingresa un valor numerico")        
            
  
def menuCoordinador():
    while True:
        try:
            jsonsfunciones.limpiarTerminal()
            print("-------------------------------------")
            print("-------Bienvenido Coordinardor-------")
            print("-------------------------------------") 
            print("Selecciona lo que deseas realizar:")
            print("1. Modificar datos Campers")
            print("2. Modificar rutas")
            print("3. Registrar Trainers")
            print("4. Reportes")
            print("0. Salir al menú anterior")
            opcion = int(input("\n Opción: "))
            if opcion==1:
                jsonsfunciones.limpiarTerminal()
                while True:
                    print("-------------------------------------")
                    print("-------Modificar datos Campers-------")
                    print("-------------------------------------")
                    print("Selecciona lo que deseas realizar:")
                    print("1. Ingresar Nota de prueba Ingreso")
                    print("2. Asignar un salón y ruta a los estudiantes")
                    print("0. Salir al menú anterior")
                    campers=int(input("\n Opción: "))
                    if campers==1:
                        jsonsfunciones.limpiarTerminal()
                        coordinador.primeraprueba()
                    elif campers==2:
                        jsonsfunciones.limpiarTerminal()
                        coordinador.asignarsalon()
                    elif campers==0:
                        jsonsfunciones.limpiarTerminal()
                        print("...Saliendo....")
                        break
                    else:
                        print("Elie una de las opciones dadas anteriormente")
            elif opcion==2:
                jsonsfunciones.limpiarTerminal()
                while True:
                    print("-------------------------------------")
                    print("-----------Modificar Rutas-----------")
                    print("-------------------------------------")
                    print("Selecciona lo que deseas realizar:")
                    print("1. Crear un Tema/Modulo ")
                    print("2. Crear una Ruta ")
                    print("3. Asignar ruta a las aulas ")
                    print("0. Salir al menú anterior")
                    rutas=int(input("\n Opción: "))
                    if rutas==1:
                        jsonsfunciones.limpiarTerminal()
                        coordinador.CrearTema()
                    elif rutas==2:
                        jsonsfunciones.limpiarTerminal()
                        coordinador.CrearRuta()
                    elif rutas==3:
                        jsonsfunciones.limpiarTerminal()                     
                        coordinador.asignarruta()
                    elif rutas==0:
                        jsonsfunciones.limpiarTerminal()
                        print("....Saliendo.....")
                        break
                    else:
                        print("Elije una opción correcta, intentalo nuevamente")
            elif opcion==3:
                jsonsfunciones.limpiarTerminal()
                while True:
                    print("-------------------------------------")
                    print("----------Registrar Trainer----------")
                    print("-------------------------------------")
                    print("Selecciona lo que deseas realizar:")
                    print("1. Registrar Trainer ")
                    print("0. Salir al menú anterior")
                    trainer=int(input("\n Opción: "))
                    if trainer==1:
                        jsonsfunciones.limpiarTerminal()
                        coordinador.registroTrainer()
                    elif trainer==0:
                        jsonsfunciones.limpiarTerminal()
                        print(".....Saliendo......")
                        break
                    else:
                        print("Elije una opción correcta.")
            elif opcion==4:
                jsonsfunciones.limpiarTerminal()
                while True:
                    print("-------------------------------------")
                    print("----------Modulo Reportes----------")
                    print("-------------------------------------")
                    print("Selecciona lo que deseas realizar:")
                    print("1. Listar los campers en estado inscrito ")
                    print("2. Listar los campers que aprobaron el examen inicial ")
                    print("3. Listar los entrenadores que se encuentran trabajando en CampusLands ")
                    print("4. Listar los campers que cuentan con bajo rendimiento")
                    print("5. Listar los campers y trainers que se encuentren asociados a una ruta de entrenamiento.")
                    print("6. Mostrar cuántos campers perdieron y aprobaron cada uno de los módulos teniendo en cuenta la ruta de entrenamiento y el entrenador encargado")
                    print("0. Salir al menú anterior")
                    reporte=int(input("\n Opción: "))
                    if reporte==1:
                        jsonsfunciones.limpiarTerminal()  
                        campersprogram.campersInscritos()
                    elif reporte==2:
                        jsonsfunciones.limpiarTerminal()
                        campersprogram.campersAprobados()
                    elif reporte==3:
                        jsonsfunciones.limpiarTerminal()
                        campersprogram.trainersInCampus()
                    elif reporte==4:
                        jsonsfunciones.limpiarTerminal()
                        campersprogram.campersRendimientoBajo()
                    elif reporte==5:
                        jsonsfunciones.limpiarTerminal()
                        campersprogram.campersYtrainersEnUnaRuta()
                    elif reporte==6:
                        jsonsfunciones.limpiarTerminal()
                        campersprogram.campersPorModulo
                    elif reporte==0:
                        jsonsfunciones.limpiarTerminal()
                        print("....Saliendo.....")
                        break
                    else:
                        print("Elije una de las opciones indicadas.")
            elif opcion==0:
                jsonsfunciones.limpiarTerminal()
                print("...Saliendo...")
                break
            else:
                print("la opción seleccionada no corresponde, intentalo de nuevo ")
        except ValueError:
            print("Elije una opción numerica.")
            
def menuTrainer():
    while True:
        try:
            jsonsfunciones.limpiarTerminal()
            print("-------------------------------------")
            print("---------Bienvenido Trainer----------")
            print("-------------------------------------") 
            print("Selecciona lo que deseas realizar:")
            print("1. Asignar notas a modulos")
            print("0. Salir al menú anterior")
            opcion = int(input("\n Opción: "))
            if opcion==1:
                jsonsfunciones.limpiarTerminal()
                trainer.notamodulo()
            elif opcion==0:
                jsonsfunciones.limpiarTerminal()
                print("....Saliendo....")
                break
        except ValueError:
            print("Elije una opción numerica.")