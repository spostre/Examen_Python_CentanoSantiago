import utils.corefiles as core
import utils.screen as screen
import main as main
from data.config import hamburguesa, chefs
chefs_data = core.readDataFile(chefs)

def add_ham():
    screen.limpiar_pantalla()
    ham_data = core.readDataFile(hamburguesa)


    print('Que hamburguesa quieres agregar?')
    print('1. Clasica')
    print('2. Vegetariana')
    print('3. Doble carne')
    print('4. Salir')

    rep = True
    id_ham = f"C{len(ham_data) + 1:03d}"

    while rep == True:
        try:
            op = int(input('opcion : '))

            if (op == 1):
                    
                    if (op in ham_data.values()):

                        print(f'{op} ya existe')
                        screen.pausar()
                        add_ham()

                    else:
                        
                        for ing in chefs_data.items():
                            print(f"{ing[0]}")
                        key_h = input("Seleccione el chef: ").upper()

                        clasic = {
                            "nombre": "Clasica",
                            "categoria": "Clasica",
                            "ingredientes": ["Pan", "Carne de res", "Queso cheddar", "Lechuga", "Tomate", "Cebolla", "Mayonesa", "Ketchup"],
                            "precio": 10,
                            "chef": key_h
                            }

                        ham_data[id_ham] = clasic

                        core.writeDataFile(hamburguesa, ham_data)
                        break

            elif (op == 2):
                    if (op in ham_data.values()):

                        print(f'{op} ya existe')
                        screen.pausar()
                        add_ham()

                    else:

                        for ing in chefs_data.items():
                            print(f"{ing[0]}")
                        key_h = input("Seleccione el chef: ").upper()

                        vegetal = {
                            "nombre": "Vegetariana",
                            "categoria": "Vegetariana",
                            "ingredientes": ["Pan integral", "Hamburguesa de lentejas", "Queso suizo", "Espinacas", "Cebolla morada", "Aguacate", "Mayonesa vegana"],
                            "precio": 8,
                            "chef": key_h
                        }

                        ham_data[id_ham] = vegetal

                        core.writeDataFile(hamburguesa, ham_data)
                        break

            elif (op == 3):
                    if (op in ham_data.values()):

                        print(f'{op} ya existe')
                        screen.pausar()
                        add_ham()

                    else:
                        
                        for ing in chefs_data.items():
                            print(f"{ing[0]}")
                        key_h = input("Seleccione el chef: ").upper()

                        gourmet = {
                            "nombre": "Doble Carne",
                            "categoria": "Gourmet",
                            "ingredientes": ["Pan de sesamo", "Doble carne de res", "Queso cheddar", "Bacon", "Lechuga", "Cebolla caramelizada", "Salsa BBQ"],
                            "precio": 12,
                            "chef": key_h
                        }

                        ham_data[id_ham] = gourmet

                        core.writeDataFile(hamburguesa, ham_data)

                        break

            elif (op == 4):
                main.main()

        except ValueError:
            print('Opcion no valida')
            screen.pausar()
            continue

    print('Hamburguesa cocinada con exito')

    screen.pausar()
    main.main()