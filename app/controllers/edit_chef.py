import utils.corefiles as core
import utils.screen as screen
import main as main
from data.config import chefs


def edit_menu():
    screen.limpiar_pantalla()
    chefs_data = core.readDataFile(chefs)
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

    global key_chef

    chefs_data = core.readDataFile(chefs)

    chef = input("Ingrese el nuevo nombre del ingrediente: ")

    chefs_data[key_chef]['precio'] = chef
    
    core.writeDataFile(chefs, chefs_data)
    
    print(f"Precio actualizado a {chef}'!")
    screen.pausar()
    main.main()

def edit_esp():
    global key_chef
    ingredientes_data = core.readDataFile(chefs)

    while True:
        try:
            stock = int(input("Ingrese el nuevo stock (si el stock es de 0 sera eliminado: )"))
            if (stock > 0):

                ingredientes_data[key_chef]['stock'] = stock

                core.writeDataFile(chefs, ingredientes_data)

                print(f"Stock actualizado")
                screen.pausar()
                main.main()
            elif (stock == 0):

                print('Stock actualizado a 0. Debido a que no hay mas existencias el ingrediente sera borrado')
                del ingredientes_data[key_chef]

                core.writeDataFile(chefs, ingredientes_data)
                screen.pausar()
                break
        except ValueError:
            print("Entrada no válida. Ingrese un número entero.")
    

def edit_libro_genero():
    global key_libro
    libros_data = core.readDataFile(libros)

    print("Ingrese el género del libro:\n1. Fantasía\n2. Ciencia\n3. Romance\n4. Misterio\n5. Accion ")
    genero = int(input('Seleccione una opcion: '))
    if (genero == 1):
        genero = 'Fantasia'
    elif (genero == 2):
        genero = 'Ciencia'
    elif (genero == 3):
        genero = 'Romance'
    elif (genero == 4):
        genero = 'Misterio'
    elif (genero == 5):
        genero = 'Acción'
    else:
        print("Opción no válida. Intente de nuevo.")
        screen.pausar_pantalla()
        edit_libro_genero()

    libros_data[key_libro]['genero'] = genero
    core.writeDataFile(libros, libros_data)

    print(f"¡Género del libro con ID '{key_libro}' actualizado!")
    screen.pausar_pantalla()
    main.main()