#menú principal 
import menus
print("Bienvenido a su sistema Campuslands")
print("Por favor elije tu Rol en Campus")
while True:
    try:
        opcion=int(input("1.) Camper \n2.) Trainer \n3.) Coordinador \n0.)Para Salir"))
        if opcion==1:
            menus.menuCamper()
        if opcion==2:
            menus.menuTrainer()
        if opcion==3:
            menus.menuCoodinador()
        if opcion==4:
            break
    except Exception:
        print("Por favor intentalo de nuevo.")