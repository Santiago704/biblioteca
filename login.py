import mysql.connector
from BD.conexion import DAO

class login():
    def beginLogin(self):
        conexion = DAO()
        cursor = conexion.conexion.cursor()
        idUsuario = input('Digite la contraseña: ') 
        nomUsuario = input('Digite el nombre de usuario: ') 
        try:
            cursor.execute("SELECT * FROM usuario WHERE nomUsuario=%s AND idUsuario=%s",(nomUsuario,idUsuario))
            usuario = cursor.fetchone()
            if usuario:
                print("Inicio de sesión")
                return True
            else:
                print("Datos incorrectos")
                return False
        except mysql.connector.Error as Ex:
            print(f'Datos incorrectos {Ex}')

        
