import utils.corefiles as core
import utils.screen as screen
import main as main
from data.config import chefs
from controllers import edit_chef as editC


def menu_chef():
    screen.limpiar_pantalla()

    print('Que aspecto de los chefs quiere gestionar')
    print('1. Agregar chef')
    print('2. Editar info del chef')
    print('3. Lista de chefs')
    print('4. Salir')

    opcion = int(input('opcion :'))

    if (opcion == 1):
        add_chef()
    elif (opcion == 2):
        editC.edit_menu()
    elif (opcion == 3):
        list_chef()
    elif (opcion == 4):
        main.main()
    else:
        print('opcion no valida')
        screen.pausar()
        menu_chef() 


def add_chef():
    screen.limpiar_pantalla()
    chefs_data = core.readDataFile(chefs)

    print('Que especialidad tiene el chef?')
    print('1. Carnes')
    print('2. Cocina vegetariana')
    print('3. Gourmet')
    print('4. Salir')

    rep = True


    while rep == True:
        try:
            op = int(input('opcion : '))

            if (op == 1):
                nombre = input('Ingrese el nombre del chef')
                especialidad = "carnes"

                rep = False

            elif (op == 2):
                nombre = input('Ingrese el nombre del chef')
                especialidad = "cocina vegetariana"
                
                rep = False

            elif (op == 3):
                nombre = input('Ingrese el nombre del chef')
                especialidad = "gourmet"
                
                rep = False

            elif (op == 4):
                main.main()

        except ValueError:
            print('Opcion no valida')
            screen.pausar()
            continue

    id_chef = f"I{len(chefs_data) + 1:03d}"

    

    if (op in chefs_data.values()):

        print(f'{op} ya existe')
        screen.pausar()
        add_chef()

    else:

        chef = {
            "nombre": nombre,
            "especialidad": especialidad
        }

        chefs_data[id_chef] = chef

        core.writeDataFile(chefs, chefs_data)

    print('Chef registrado con exito')

    screen.pausar()
    main.main()

def list_chef():
    screen.limpiar_pantalla()
    chef_data = core.readDataFile(chefs)

    for chef in chef_data.values():

        print([chef['nombre'], chef['especialidad']])
            
    screen.pausar()
    main.main()