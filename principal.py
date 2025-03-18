# Importacion de ficheros
#from login import beginLogin
from register import register

# Definicion del menu principal
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

# Funcion para ejecutar la opcion seleccionada
def executeOption(option):
    if option ==1:
        print('hola')
        # try:
        #     users = DAO.listUsers()
        #     if len(users)>0:
        #         #Falta ejecutar
        #     else:
        #         print('No se ha encontrado usuarios')
        # except:
        #     print('Ocurrio un error')
    elif option ==2:
        user_registration = register()
        user_registration.new_user()

firstMenu()