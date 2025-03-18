#Importacion de ficheros
from login import beginLogin

#Definicion del menu principal
def firstMenu():
    continueIn = True
    while(continueIn):
        correctOption = False
        while(not correctOption):
            print('======= MENU PRINCIPAL ======')
            print('1. Ingresar')
            print('2. Registrarse')
            print('3. Salir')
            print('=============================')
            option = int(input('Seleccioneuna opcion'))

            if option <1 or option>3:
                print('Opcion incorrecta, ingrese nuevamente')
            elif option ==3:
                continueIn = False
                print('¡Gracias por usar este sistema¡')
                break
            else:
                correctOption = True
                executeOption(option)

def executeOption(option):
    print(option)

firstMenu()