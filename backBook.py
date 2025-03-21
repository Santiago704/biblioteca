import mysql.connector
from BD.conexion import DAO

class backBook():
    def back(self):
        conexion = DAO()
        cursor = conexion.conexion.cursor()
        name_book_to_back = input('Digite el nombre del libro que deseas regresar: ')
        try:
            cursor.execute("SELECT * FROM libro WHERE nomLibro=%s AND activo='NO'",(name_book_to_back,))
            book = cursor.fetchone()
            if book:
               print(f'El libro {name_book_to_back} ha sido regresado con exito')
               cursor.execute("UPDATE libro SET activo='SI' WHERE nomLibro=%s",(name_book_to_back,))
               conexion.conexion.commit()
            else:
                print(f"Libro {name_book_to_back} no encontrado pra devolucion")
        except mysql.connector.Error as Ex:
            print(f'Datos incorrectos {Ex}')