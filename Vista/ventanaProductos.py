from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui
from Modelo.arregloProductos import ArregloProductos
from Modelo.conexionProductos import ConexionProductos
from Controlador.productos import Producto

aPro = ArregloProductos()
productos = ConexionProductos()

class VentanaProductos(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(VentanaProductos,self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon("UI/imagenes/venta.png"))
        uic.loadUi("UI/ventanaProductos.ui",self)
       
        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnConsultar.clicked.connect(self.consultar)
        self.btnListar.clicked.connect(self.listar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnModificar.clicked.connect(self.modificar)
        self.btnGrabar.clicked.connect(self.grabar)
        self.listar()
        self.show()
        #self.txtCodigo.setEnabled(False)

    def obtenerCodigo(self):
        return self.txtCodigo.text()
    
    def obtenerNombre(self):
        return self.txtNombre.text()
    
    def obtenerDescripcion(self):
        return self.txtDescripcion.text()
    
    def obtenerMinimo(self):
        return self.txtStockMinimo.text()
    
    def obtenerActual(self):
        return self.txtStockActual.text()
    
    def obtenerCosto(self):
        return self.txtPrecioCosto.text()

    def obtenerPrecio(self):
        return self.txtPrecioVenta.text()

    def obtenerProveedor(self):
        return self.cboProveedor.currentText()
    
    def obtenerAlmacen(self):
        return self.cboAlmacen.currentText()

    def limpiarTabla(self):
        self.tblProductos.clearContents()
        self.tblProductos.setRowCount(0)

    def valida(self):
        if self.txtNombre.text() == "":
            self.txtNombre.setFocus()
            return "Nombre del producto...!!!"
        elif self.txtDescripcion.text() == "":
            self.txtDescripcion.setFocus()
            return "Descripción del producto...!!!"
        elif self.txtStockMinimo.text() == "":
            self.txtStockMinimo.setFocus()
            return "Stock mínimo del producto...!!!"
        elif self.txtStockActual.text() == "":
            self.txtStockActual.setFocus()
            return "Stock máximo del producto...!!!"
        elif self.txtPrecioCosto.text() == "":
            self.txtPrecioCosto.setFocus()
            return "Costo del producto...!!!"
        elif self.txtPrecioVenta.text() == "":
            self.txtPrecioVenta.setFocus()
            return "Precio del producto...!!!"
        elif self.cboProveedor.currentText() == "Seleccionar Proveedor":
            self.cboProveedor.setCurrentIndex(0)
            return "Proveedor...!!!"
        elif self.cboAlmacen.currentText() == "Seleccionar Almacén":
            self.cboAlmacen.setCurrentIndex(0)
            return "Almacén...!!!"
        else:
            return ""

    def listar(self):
        i = 0
        respuesta = productos.listar_productos()
        self.tblProductos.setRowCount(len(respuesta))
        self.tblProductos.setColumnCount(9)
        self.tblProductos.verticalHeader().setVisible(False)
        for fila in respuesta:
            self.tblProductos.setItem(i, 0, QtWidgets.QTableWidgetItem(str(fila[0])))
            self.tblProductos.setItem(i, 1, QtWidgets.QTableWidgetItem(fila[1]))
            self.tblProductos.setItem(i, 2, QtWidgets.QTableWidgetItem(fila[2]))
            self.tblProductos.setItem(i, 3, QtWidgets.QTableWidgetItem(str(fila[3])))
            self.tblProductos.setItem(i, 4, QtWidgets.QTableWidgetItem(str(fila[4])))
            self.tblProductos.setItem(i, 5, QtWidgets.QTableWidgetItem(str(fila[5])))
            self.tblProductos.setItem(i, 6, QtWidgets.QTableWidgetItem(str(fila[6])))
            self.tblProductos.setItem(i, 7, QtWidgets.QTableWidgetItem(fila[7]))
            self.tblProductos.setItem(i, 8, QtWidgets.QTableWidgetItem(fila[8]))
            i = i + 1

    def limpiarControles(self):
        self.txtCodigo.clear()
        self.txtNombre.clear()
        self.txtDescripcion.clear()
        self.txtStockMinimo.clear()
        self.txtStockActual.clear()
        self.txtPrecioCosto.clear()
        self.txtPrecioVenta.clear()
        self.cboProveedor.setCurrentIndex(0)
        self.cboAlmacen.setCurrentIndex(0)

    def registrar(self):
        if self.valida() == "":
            datos = (self.obtenerNombre(), self.obtenerDescripcion(), self.obtenerMinimo(), self.obtenerActual(), self.obtenerCosto(), self.obtenerPrecio(), self.obtenerProveedor(), self.obtenerAlmacen())
            productos.agregar_producto(datos)
            self.limpiarControles()
            self.listar()
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Producto", "Error en " + self.valida(), QtWidgets.QMessageBox.Ok)

    def consultar(self):
        self.limpiarTabla()
        if len(productos.listar_productos()) == 0:
            QtWidgets.QMessageBox.information(self, "Consultar Producto", "No existen productos a consultar...!!!", QtWidgets.QMessageBox.Ok)
        else:
            codigo, _ = QtWidgets.QInputDialog.getText(self, "Consultar Producto", "Ingrese el código a consultar")
            respuesta = productos.consultar_productos(codigo)
            if len(respuesta) <= 0:
                QtWidgets.QMessageBox.information(self, "Consultar Producto", "El código ingresado no existe...!!! ", QtWidgets.QMessageBox.Ok)
            else:
                self.tblProductos.setRowCount(1)
                self.tblProductos.setItem(0, 0, QtWidgets.QTableWidgetItem(codigo))
                self.tblProductos.setItem(0, 1, QtWidgets.QTableWidgetItem(respuesta[0][0]))
                self.tblProductos.setItem(0, 2, QtWidgets.QTableWidgetItem(respuesta[0][1]))
                self.tblProductos.setItem(0, 3, QtWidgets.QTableWidgetItem(str(respuesta[0][2])))
                self.tblProductos.setItem(0, 4, QtWidgets.QTableWidgetItem(str(respuesta[0][3])))
                self.tblProductos.setItem(0, 5, QtWidgets.QTableWidgetItem(str(respuesta[0][4])))
                self.tblProductos.setItem(0, 6, QtWidgets.QTableWidgetItem(str(respuesta[0][5])))
                self.tblProductos.setItem(0, 7, QtWidgets.QTableWidgetItem(respuesta[0][6]))
                self.tblProductos.setItem(0, 8, QtWidgets.QTableWidgetItem(respuesta[0][7]))

    def eliminar(self):
        if len(productos.listar_productos()) == 0:
            QtWidgets.QMessageBox.information(self, "Eliminar Producto", "No existen productos a eliminar...!!!", QtWidgets.QMessageBox.Ok)
        else:
            fila = self.tblProductos.selectedItems()
            if fila:
                indiceFila = fila[0].row()
                codigo = self.tblProductos.item(indiceFila, 0).text()
                productos.eliminar_producto(codigo)   
                self.limpiarTabla()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Eliminar Producto", "Debe seleccionar una fila...!!!", QtWidgets.QMessageBox.Ok)

    def modificar(self):
        if len(productos.listar_productos()) == 0:
            QtWidgets.QMessageBox.information(self, "Modificar Producto", "No existen productos a modificar...!!!", QtWidgets.QMessageBox.Ok)
        else:
            codigo, _ = QtWidgets.QInputDialog.getText(self, "Modificar Producto", "Ingrese el código a modificar")
            respuesta = productos.consultar_productos(codigo)
            if len(respuesta) > 0:
                self.btnModificar.setVisible(False)
                self.btnGrabar.setVisible(True)
                #self.txtCodigo.setEnabled(False)
                self.txtCodigo.setText(codigo)
                self.txtNombre.setText(respuesta[0][0])
                self.txtDescripcion.setText(respuesta[0][1])
                self.txtStockMinimo.setText(str(respuesta[0][2]))
                self.txtStockActual.setText(str(respuesta[0][3]))
                self.txtPrecioCosto.setText(str(respuesta[0][4]))
                self.txtPrecioVenta.setText(str(respuesta[0][5]))
                self.cboProveedor.setCurrentText(respuesta[0][6])
                self.cboAlmacen.setCurrentText(respuesta[0][7])
        
    def grabar(self):
        try:
            datos = (self.obtenerNombre(), self.obtenerDescripcion(), self.obtenerMinimo(), self.obtenerActual(), self.obtenerCosto(), self.obtenerPrecio(), self.obtenerProveedor(), self.obtenerAlmacen(), self.obtenerCodigo())
            respuesta = productos.modificar_productos(datos)
            self.btnModificar.setVisible(True)
            self.btnGrabar.setVisible(False)
            self.limpiarTabla()
            self.limpiarControles()
            self.listar()
            self.txtCodigo.setVisible(True)
            self.lblCodigo.setVisible(True)
        except:
            QtWidgets.QMessageBox.information(self, "Modificar Producto", "Error al modificar producto...!!!", QtWidgets.QMessageBox.Ok)