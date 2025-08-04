import utils.corefiles as core
import utils.screen as screen
import main as main
from data.config import chefs
from controllers import edit_ing as editI


def menu_ing():
    screen.limpiar_pantalla()

    print('Que aspecto de los ingredientes quiere gestionar')
    print('1. Crear ingrediente')
    print('2. Modificar ingrediente')
    print('3. Listar ingredientes')
    print('4. Salir')

    opcion = int(input('opcion :'))

    if (opcion == 1):
        add_ing()
    elif (opcion == 2):
        editI.edit_menu()
    elif (opcion == 3):
        list_ing()
    elif (opcion == 4):
        main.main()
    else:
        print('opcion no valida')
        screen.pausar()
        menu_ing() 


def add_ing():
    screen.limpiar_pantalla()
    ingredientes_data = core.readDataFile(chefs)

    print('Que ingrediente desea añadir?')
    print('1. Pan')
    print('2. Carne de res')
    print('3. Queso cheddar')
    print('4. Salir')

    rep = True


    while rep == True:
        try:
            nombre = int(input('opcion : '))

            if (nombre == 1):
                nombre = "pan"
                desc = "pan de hamburguesa clasico"
                precio = 2.5
                stock = 500

                rep = False

            elif (nombre == 2):
                nombre = "carne de res"
                desc = "carne de res jugosa y sabrosa"
                precio = 8
                stock = 300
                
                rep = False

            elif (nombre == 3):
                nombre = "queso cheddar"
                desc = "queso cheddar derretido"
                precio = 1.5
                stock = 200
                
                rep = False

            elif (nombre == 4):
                main.main()

        except ValueError:
            print('Opcion no valida')
            screen.pausar()
            continue

    id_ing = f"I{len(ingredientes_data) + 1:03d}"

    

    if (nombre in ingredientes_data.values()):

        print(f'{nombre} ya se encuentra en ingredientes')
        screen.pausar()
        add_ing()

    else:

        ingrediente = {
            "nombre": nombre,
            "descripcion": desc,
            "precio": precio,
            "stock": stock
        }

        ingredientes_data[id_ing] = ingrediente

        core.writeDataFile(chefs, ingredientes_data)

    print('Ingrediente añadido con exito')

    screen.pausar()
    main.main()

def list_ing():
    screen.limpiar_pantalla()
    ingredientes_data = core.readDataFile(chefs)

    for ing in ingredientes_data.values():

        print([ing['nombre'], ing['descripcion'], ing['precio'], ing['stock']])
            
    screen.pausar()
    main.main()