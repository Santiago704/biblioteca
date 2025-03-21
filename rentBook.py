import mysql.connector
from BD.conexion import DAO

class rentBook():
    def rent(self):
        conexion = DAO()
        cursor = conexion.conexion.cursor()
        name_book = input('Digite el nombre del libro que deseas prestar: ')
        try:
            cursor.execute("SELECT * FROM libro WHERE nomLibro=%s AND activo='SI'",(name_book,))
            book = cursor.fetchone()
            if book:
               print(f'El libro {name_book} prestara por 15 dias')
               cursor.execute("UPDATE libro SET activo='NO' WHERE nomLibro=%s",(name_book,))
               conexion.conexion.commit()
            else:
                print(f"Libro {name_book} no encontrado")
                return False
        except mysql.connector.Error as Ex:
            print(f'Datos incorrectos {Ex}')