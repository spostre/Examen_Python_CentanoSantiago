import utils.corefiles as core
import utils.screen as screen
import main as main
from data.config import hamburguesa


def edit_menu():
    screen.limpiar_pantalla()
    chefs_data = core.readDataFile(hamburguesa)
    global key_chef
    
    print('Que chef deseas editar?')
    for chef in chefs_data.items():
        print(f"{chef[0]}")

    while True:
        try:
            key_chef = input("Seleccione el chef a editar: ").upper()

            if (key_chef in chefs_data):
                screen.limpiar_pantalla()

                print(f"Chef seleccionado: {chefs_data[key_chef]['nombre']}")
                print("¿Qué aspecto del chef desea editar?")
                print("1. Nombre")
                print("2. Especialidad")
                print("3. salir")

                while True:
                    try:
                        sub_opcion = int(input("Seleccione una opción: "))
                        if sub_opcion == 1:
                            edit_nombre()
                        elif sub_opcion == 2:
                            edit_esp()
                        elif sub_opcion == 3:
                            main.main()
                        else:
                            print("Opción no válida. Intente de nuevo.")
                    except ValueError:
                        print("Entrada no válida. Por favor, ingrese un número.")
            else:
                print("Codigo no valido. Intente de nuevo.")
                continue

        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número o el título del libro.")

def edit_nombre():
    screen.limpiar_pantalla()

    global key_chef

    chefs_data = core.readDataFile(hamburguesa)

    chef = input("Ingrese el nuevo nombre del ingrediente: ")

    chefs_data[key_chef]['precio'] = chef
    
    core.writeDataFile(hamburguesa, chefs_data)
    
    print(f"Precio actualizado a {chef}'!")
    screen.pausar()
    main.main()

def edit_esp():
    screen.limpiar_pantalla()

    global key_chef
    chefs_data = core.readDataFile(hamburguesa)

    print("Ingrese la especialidad del chef:\n1. carnes\n2. cocina vegetariana\n3. gourmet\n4. fritos\n5. postres ")
    especialisacion = int(input('Seleccione una opcion: '))
    if (especialisacion == 1):
        especialisacion = 'carnes'
    elif (especialisacion == 2):
        especialisacion = 'cocina vegetariana'
    elif (especialisacion == 3):
        especialisacion = 'gourmet'
    elif (especialisacion == 4):
        especialisacion = 'fritos'
    elif (especialisacion == 5):
        especialisacion = 'postres'
    else:
        print("Opción no válida. Intente de nuevo.")
        screen.pausar()
        edit_esp()

    chefs_data[key_chef]['especialisacion'] = especialisacion
    core.writeDataFile(hamburguesa, chefs_data)

    print(f"Especialidad del chef actualizada")
    screen.pausar()
    main.main()
    

