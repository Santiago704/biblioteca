import mysql.connector
from mysql.connector import Error

class DAO():
    #Conexion a la base de datos
    def __init__(self):
        try:
            self.conexion=mysql.connector.connect(
                host='localhost'
                port=3306
                user='root'
                password='root'
                db='biblioteca'
            )
        except Error as ex:
            print("Error al intentar la conexion")
    
    #Listar usuarios
    def listarUsuarios(self):
        if self.conexion.is_connected:
            try:
                cursor=self.conexion.cursor()
                cursor.execute("SELECT * FROM usuario ORDER BY nomUsuario ASC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexion")
