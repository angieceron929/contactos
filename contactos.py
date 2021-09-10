from bd import conexion
from datetime import datetime, date, time, timedelta

class RegistroCont():
    def insertarCont(self,iden,nombre,apellidos,email,celular):
        conexions = conexion()
        with conexions.cursor() as cursor:
        
            cursor.execute("""insert into contactos(
                identificacion,
                nombres,
                apellidos,
                email,
                celular
            )values (%s ,%s ,%s ,%s ,%s )
             """, (iden,nombre,apellidos,email,celular,))
        conexions.commit()
        conexions.close()
    
    def Listado(self):
        conexions = conexion()
        contacts = []
        with conexions.cursor() as cursor:

            sql = """select * from contactos """
            cursor.execute(sql)
            contacts = cursor.fetchall()
        conexions.close()
        return contacts

    def EliminarCont(self,id):
        conexions = conexion()
        with conexions.cursor() as cursor:
            cursor.execute(""" Delete FROM contactos Where id = %s  """, (id,))
        conexions.commit()
        cursor.close()

    def ActualizarCont(self,iden,nombre,apellidos,email,celular,id):
        conexions= conexion()
        with conexions.cursor() as cursor:
            cursor.execute(""" update contactos set identificacion = %s  , nombres = %s  , apellidos = %s , email = %s ,celular = %s  where id = %s  """,(iden,nombre,apellidos, email,celular,id,))
        conexions.commit()
        conexions.close()

    def EditarCont(self,id):
        conexions = conexion()
        contacto = None
        with conexions.cursor() as cursor:
            cursor.execute(""" select * from contactos 
            where id = %s """,(id,))
            contacto = cursor.fetchone()
        
        conexions.close()
        return contacto




