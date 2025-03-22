# Importacion de ficheros
from login import login
from register import register
from newBook import newBook
from rentBook import rentBook
from backBook import backBook

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
        user_login = login()
        user_login.beginLogin()
        secondMenu()
    elif option ==2:
        user_registration = register()
        user_registration.new_user()
        secondMenu()

# Funcion para mostrar el segundo menu
def secondMenu():
    continueIn = True
    while(continueIn):
        correctOption = False
        while(not correctOption):
            print('======= MENU SECUNDARIO ======')
            print('1. Ingresar nuevo libro')
            print('2. Hacer prestamo de un libro')
            print('3. Devolver libro')
            print('4. Volver al menu inicial')
            print('=============================')
            option = int(input('Seleccioneuna opcion'))

            if option <1 or option>4:
                print('Opcion incorrecta, ingrese nuevamente')
            elif option ==4:
                continueIn = False
                print('Voliste al menu inicial')
                break
            else:
                correctOption = True
                executeOptionSecondMenu(option)

# Funcion para ejecutar la opcion seleccionada del segundo menu
def executeOptionSecondMenu(option):
    if option ==1:
        new_book = newBook()
        new_book.new_book_added()
    elif option ==2:
        rent = rentBook()
        rent.rent()
    elif option ==3:
        back = backBook()
        back.back()

firstMenu()