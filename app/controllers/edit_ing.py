import utils.corefiles as core
import utils.screen as screen
import main as main
from data.config import hamburguesa


def edit_menu():
    screen.limpiar_pantalla()
    ingredientes_data = core.readDataFile(hamburguesa)
    global key_ing
    
    print('Que ingrediente deseas editar?')
    for ing in ingredientes_data.items():
        print(f"{ing[0]}")

    while True:
        try:
            key_ing = input("Seleccione el ingrediente a editar: ").upper()

            if (key_ing in ingredientes_data):
                screen.limpiar_pantalla()

                print(f"Ingrediente seleccionado: {ingredientes_data[key_ing]['nombre']}")
                print("¿Qué aspecto del ingrediente desea editar?")
                print("1. Precio")
                print("2. Stock")
                print("3. salir")

                while True:
                    try:
                        sub_opcion = int(input("Seleccione una opción: "))
                        if sub_opcion == 1:
                            edit_precio()
                        elif sub_opcion == 2:
                            edit_stock()
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

def edit_precio():

    global key_ing

    ingredientes_data = core.readDataFile(hamburguesa)

    precio = input("Ingrese el nuevo precio del ingrediente: ")

    ingredientes_data[key_ing]['precio'] = precio
    
    core.writeDataFile(hamburguesa, ingredientes_data)
    
    print(f"Precio actualizado a {precio}'!")
    screen.pausar()
    main.main()

def edit_stock():
    global key_ing
    ingredientes_data = core.readDataFile(hamburguesa)

    while True:
        try:
            stock = int(input("Ingrese el nuevo stock (si el stock es de 0 sera eliminado: )"))
            if (stock > 0):

                ingredientes_data[key_ing]['stock'] = stock

                core.writeDataFile(hamburguesa, ingredientes_data)

                print(f"Stock actualizado")
                screen.pausar()
                main.main()
            elif (stock == 0):

                print('Stock actualizado a 0. Debido a que no hay mas existencias el ingrediente sera borrado')
                del ingredientes_data[key_ing]

                core.writeDataFile(hamburguesa, ingredientes_data)
                screen.pausar()
                break
        except ValueError:
            print("Entrada no válida. Ingrese un número entero.")
    

