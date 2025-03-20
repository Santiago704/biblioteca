import mysql.connector
from BD.conexion import DAO

class newBook():
    def new_book_added(self):
        conexion = DAO()
        cursor = conexion.conexion.cursor()
        #codLibro = int(input('digite el codigo del libro'))
        nomLibro = input('Digite el nombre del libro: ')
        genero = input(f'Digite el geneto de {nomLibro}: ')
        autor = input(f'Digite el autor de {nomLibro}: ')

        try:
            cursor.execute("INSERT INTO libro (nomLibro, genero, autor) VALUES(%s, %s, %s)", (nomLibro, genero, autor))
            conexion.conexion.commit()
            print(f'{nomLibro} registrado con exito')
        except mysql.connector.IntegrityError:
            print('Libro no registrado')