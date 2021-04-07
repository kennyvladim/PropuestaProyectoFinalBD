import sqlite3

class ConexionClientes:

    def conectar(self):
        try:
            conexion = sqlite3.connect("D:\PropuestaProyectoFinalBD\Modelo\productos.db") 
        except:
            print("No se ha podido realizar la conexion...!!!")
        return conexion

    def listar_clientes(self):
        try:
            cone = self.conectar()
            cursor = cone.cursor()
            sql = "select * from tabla_clientes"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()

    def agregar_cliente(self, datos):
        cone = self.conectar()
        cursor = cone.cursor()
        sql = "insert into tabla_clientes(Dni,Nombres,Apellido_Paterno,Apellido_Materno,Direccion,Telefono) values (?,?,?,?,?,?)" 
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def eliminar_cliente(self, dni):
        try:
            cone = self.conectar()
            cursor = cone.cursor()
            sql = "delete from tabla_clientes where Dni = ?"
            cursor.execute(sql, dni)
            cone.commit()
            return cursor.rowcount # retornamos la cantidad de filas borradas
        except:
            cone.close()
    
    def consultar_clientes(self, dni):
        try:
            cone = self.conectar()
            cursor = cone.cursor()
            sql = "select Nombres,Apellido_Paterno,Apellido_Materno,Direccion,Telefono from tabla_clientes where Dni = ?"
            cursor.execute(sql, dni)
            return cursor.fetchall()
        finally:
            cone.close()

    def modificar_clientes(self, datos):
        try:
            cone = self.conectar()
            cursor = cone.cursor()
            sql = "update tabla_clientes set Nombres = ?, Apellido_Paterno = ?, Apellido_Materno = ?, Direccion = ?, Telefono = ? where Dni = ?"
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount # retornamos la cantidad de filas modificadas            
        except:
            cone.close()