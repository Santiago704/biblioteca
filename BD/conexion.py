import mysql.connector
from mysql.connector import Error

class DAO():
    #Conexion a la base de datos
    def __init__(self):
        try:
            self.conexion=mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                database='biblioteca'
            )
        except Error as ex:
            print("Error al intentar la conexion",ex)
