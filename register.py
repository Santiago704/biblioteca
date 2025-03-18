import mysql.connector
from BD.conexion import DAO

class register():

    def new_user(self):
        conexion = DAO()
        cursor = conexion.conexion.cursor()
        idUsuario = input('Digite la contraseña: ') 
        nomUsuario = input('Digite el nombre de usuario: ') 
        dirUsuario = input('Digite la direccion del usuario: ')
        celular = input('Digite el numero celular')
        try:
            cursor.execute("INSERT INTO usuario (idUsuario, nomUsuario, dirUsuario, celular) VALUES(%s, %s, %s, %s)", (idUsuario, nomUsuario, dirUsuario, celular))
            conexion.conexion.commit()
            print('Usuario registrado con exito')
        except mysql.connector.IntegrityError:
            print('Usuario ya existee')

