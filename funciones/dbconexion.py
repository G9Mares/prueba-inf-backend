import mysql.connector
from pydantic import BaseModel
import time

class Usuario(BaseModel):
    id:int
    nombre:str
    correo:str
    tel:str
    password:str


class MiObjetoMySQL:
    def __init__(self, host:str, user:str, password:str, admin_user:str, admin_correo:str, admin_tel:str,admi_pass:str):
        # Establecer la conexión con la base de datos MySQL.
        self.conexion = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
        )
        # Crear el cursor.
        self.cursor = self.conexion.cursor()
        self.cursor.execute('CREATE DATABASE IF NOT EXISTS db_pruebainies')
        self.cursor.execute('USE db_pruebainies')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(60) NOT NULL,
        correo VARCHAR(60) NOT NULL,
        tel VARCHAR(20) NOT NULL,
        password VARCHAR(200) NOT NULL
            )
        ''')
        self.conexion.commit()
        self.crear_usuario(admin_user,admin_correo,admin_tel,admi_pass)

    def usuario_info_by_nombre(self,nombre:str)->Usuario|bool:
        peticion = 'SELECT * FROM usuarios WHERE nombre = %s'
        self.cursor.execute(peticion,(nombre,))
        try:
        
            result_id = self.cursor.fetchone()
            print(result_id)
            usuario_data = dict(zip(self.cursor.column_names, result_id))
            usuario = Usuario(**usuario_data)
            return usuario
        except:
            return False

    def usuario_info_by_correo(self,correo:str)->Usuario|bool:
        peticion = 'SELECT * FROM usuarios WHERE correo = %s'
        self.cursor.execute(peticion,(correo,))
        try:
            result_id = self.cursor.fetchone()
            usuario_data = dict(zip(self.cursor.column_names, result_id))
            usuario = Usuario(**usuario_data)
            return usuario
        except:
            return False
        
    

    def crear_usuario(self,nombre:str, correo:str, tel:str, password:str)->bool:
        existenia_nombre = self.usuario_info_by_nombre(nombre)
        existenia_correo = self.usuario_info_by_correo(correo)
        if existenia_correo or existenia_nombre:
            return False
        peticion = "INSERT INTO usuarios (nombre , correo , tel, password) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(peticion,(nombre,correo,tel,password))
        self.conexion.commit()
        return True
    
    def cerrar_conexion(self):
        # Cerrar el cursor y la conexión a MySQL.
        self.cursor.close()
        self.conexion.close()


sql_instance = MiObjetoMySQL(host="localhost",user='root',password='',admin_user='admin',admin_correo='correo@gmail.com',admin_tel='5540385263',admi_pass='pass123')
