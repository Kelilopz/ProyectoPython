#menú principal 
import json
import menus
print("Bienvenido a su sistema Campuslands")
print("Por favor elije tu Rol en Campus")
while True:
    try:
        opcion=int(input("1.) Camper \n2.) Trainer \n3.) Coordinador \n0.) Para Salir\n\nOpcion:   "))
        if opcion==1:
            menus.menuCamper()
        elif opcion==2:
            menus.menuTrainer()
        elif opcion==3:
            menus.menuCoordinador()
        elif opcion==0:
            break
        else:
            print("No elegiste una opción correcta")
    except Exception:
        print("Por favor intentalo de nuevo.")