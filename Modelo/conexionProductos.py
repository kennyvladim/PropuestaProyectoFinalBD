import sqlite3

class ConexionProductos:

    def conectar(self):
        try:
            conexion = sqlite3.connect("D:\PropuestaProyectoFinalBD\Modelo\productos.db") 
        except:
            print("No se ha podido realizar la conexion...!!!")
        return conexion

    def listar_productos(self):
        try:
            cone = self.conectar()
            cursor = cone.cursor()
            sql = "select * from tabla_productos"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()

    def agregar_producto(self, datos):
        cone = self.conectar()
        cursor = cone.cursor()
        sql = "insert into tabla_productos(Nombre, Descripcion, Stock_Minimo, Stock_Actual, Precio_Costo, Precio_Venta, Proveedor, Almacen) values (?,?,?,?,?,?,?,?)" 
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def eliminar_producto(self, codigo):
        try:
            cone = self.conectar()
            cursor = cone.cursor()
            sql = "delete from tabla_productos where Codigo = ?"
            cursor.execute(sql, codigo)
            cone.commit()
            return cursor.rowcount # retornamos la cantidad de filas borradas
        except:
            cone.close()
    
    def consultar_productos(self, codigo):
        try:
            cone = self.conectar()
            cursor = cone.cursor()
            sql = "select Nombre, Descripcion, Stock_Minimo, Stock_Actual, Precio_Costo, Precio_Venta, Proveedor, Almacen from tabla_productos where Codigo = ?"
            cursor.execute(sql, codigo)
            return cursor.fetchall()
        finally:
            cone.close()

    def modificar_productos(self, datos):
        try:
            cone = self.conectar()
            cursor = cone.cursor()
            sql = "update tabla_productos set Nombre = ?, Descripcion = ?, Stock_Minimo = ?, Stock_Actual = ?, Precio_Costo = ?, Precio_Venta = ?, Proveedor = ?, Almacen = ? where Codigo = ?"
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount # retornamos la cantidad de filas modificadas            
        except:
            cone.close()