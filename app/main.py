import utils.screen as screen
from controllers import ingredients as ing
from controllers import chef as chef
from controllers import hamburgesas as ham


def main():

    while True:
        opcion = menu()
        if (opcion == 1):
            ing.menu_ing()
        elif (opcion == 2):
            chef.menu_chef()
        elif (opcion == 3):
            ham.add_ham()
        elif (opcion == 4):
            pass
        elif (opcion == 5):
            pass
        elif (opcion == 6):
            pass
        elif (opcion == 7):
            pass
        elif (opcion == 8):
            print("Saliendo del programa...")
            break



def menu():
    screen.limpiar_pantalla()

    print('Hamburgueseria')

    print('1. Gestionar ingredientes')
    print('2. Gestionar chefs')
    print('3. Crear hamburguesa')
    
    while True:
        try:
            opcion = int(input("\nSeleccione una opción: "))
            if (0 <= opcion <= 3):
                return opcion
            else:
                print('saliendo')
                break
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

if __name__ == "__main__":
    main()