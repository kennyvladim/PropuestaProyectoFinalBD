from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui
from Modelo.arregloClientes import ArregloClientes
from Modelo.conexionClientes import ConexionClientes
from Controlador.clientes import Cliente

aCli = ArregloClientes()
clientes = ConexionClientes()

class VentanaClientes(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(VentanaClientes,self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon("UI/imagenes/venta.png"))
        uic.loadUi("UI/ventanaClientes.ui", self)
       
        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnConsultar.clicked.connect(self.consultar)
        self.btnListar.clicked.connect(self.listar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnModificar.clicked.connect(self.modificar)
        self.btnGrabar.clicked.connect(self.grabar)
        self.listar()
        self.show()

    def obtenerDni(self):
        return self.txtDni.text()
    
    def obtenerNombres(self):
        return self.txtNombres.text()
    
    def obtenerApellidoPaterno(self):
        return self.txtApellidoPaterno.text()
    
    def obtenerApellidoMaterno(self):
        return self.txtApellidoMaterno.text()
    
    def obtenerDireccion(self):
        return self.txtDireccion.text()
    
    def obtenerTelefono(self):
        return self.txtTelefono.text()

    def limpiarTabla(self):
        self.tblClientes.clearContents()
        self.tblClientes.setRowCount(0)

    def valida(self):
        if self.txtDni.text() == "":
            self.txtDni.setFocus()
            return "DNI del cliente...!!!"
        elif self.txtNombres.text() == "":
            self.txtNombres.setFocus()
            return "Nombre del cliente...!!!"
        elif self.txtApellidoPaterno.text() == "":
            self.txtApellidoPaterno.setFocus()
            return "Apellido Paterno del cliente...!!!"
        elif self.txtApellidoMaterno.text() == "":
            self.txtApellidoMaterno.setFocus()
            return "Apellido Materno del cliente...!!!"
        elif self.txtDireccion.text() == "":
            self.txtDireccion.setFocus()
            return "Dirección del cliente...!!!"
        elif self.txtTelefono.text() == "":
            self.txtTelefono.setFocus()
            return "Teléfono del cliente...!!!"
        else:
            return ""

    def listar(self):
        i = 0
        respuesta = clientes.listar_clientes()
        self.tblClientes.setRowCount(len(respuesta))
        self.tblClientes.setColumnCount(6)
        self.tblClientes.verticalHeader().setVisible(False)
        for fila in respuesta:
            self.tblClientes.setItem(i, 0, QtWidgets.QTableWidgetItem(fila[0]))
            self.tblClientes.setItem(i, 1, QtWidgets.QTableWidgetItem(fila[1]))
            self.tblClientes.setItem(i, 2, QtWidgets.QTableWidgetItem(fila[2]))
            self.tblClientes.setItem(i, 3, QtWidgets.QTableWidgetItem(fila[3]))
            self.tblClientes.setItem(i, 4, QtWidgets.QTableWidgetItem(fila[4]))
            self.tblClientes.setItem(i, 5, QtWidgets.QTableWidgetItem(fila[5]))
            i = i + 1

    def limpiarControles(self):
        self.txtDni.clear()
        self.txtNombres.clear()
        self.txtApellidoPaterno.clear()
        self.txtApellidoMaterno.clear()
        self.txtDireccion.clear()
        self.txtTelefono.clear()

    def registrar(self):
        if self.valida() == "":
            datos = (self.obtenerDni(), self.obtenerNombres(), self.obtenerApellidoPaterno(), self.obtenerApellidoMaterno(), self.obtenerDireccion(), self.obtenerTelefono())
            clientes.agregar_cliente(datos)
            self.limpiarControles()
            self.listar()
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Cliente", "Error en " + self.valida(), QtWidgets.QMessageBox.Ok)

    def consultar(self):

        self.limpiarTabla()
        if len(clientes.listar_clientes()) == 0:
            QtWidgets.QMessageBox.information(self, "Consultar Cliente", "No existen clientes a consultar...!!!", QtWidgets.QMessageBox.Ok)
        else:
            dni, _ = QtWidgets.QInputDialog.getText(self, "Consultar Cliente", "Ingrese el DNI a consultar")
            respuesta = clientes.consultar_clientes(dni)
            if len(respuesta) <= 0:
                QtWidgets.QMessageBox.information(self, "Consultar Cliente", "El DNI ingresado no existe...!!! ", QtWidgets.QMessageBox.Ok)
            else:
                self.tblClientes.setRowCount(1)
                self.tblClientes.setItem(0, 0, QtWidgets.QTableWidgetItem(dni))
                self.tblClientes.setItem(0, 1, QtWidgets.QTableWidgetItem(respuesta[0][0]))
                self.tblClientes.setItem(0, 2, QtWidgets.QTableWidgetItem(respuesta[0][1]))
                self.tblClientes.setItem(0, 3, QtWidgets.QTableWidgetItem(str(respuesta[0][2])))
                self.tblClientes.setItem(0, 4, QtWidgets.QTableWidgetItem(str(respuesta[0][3])))
                self.tblClientes.setItem(0, 5, QtWidgets.QTableWidgetItem(str(respuesta[0][4])))

    def eliminar(self):

        if len(clientes.listar_clientes()) == 0:
             QtWidgets.QMessageBox.information(self, "Eliminar Cliente", "No existen clientes a eliminar...!!!", QtWidgets.QMessageBox.Ok)
        else:
            fila = self.tblClientes.selectedItems()
            if fila:
                indiceFila = fila[0].row()
                dni = self.tblClientes.item(indiceFila, 0).text()
                clientes.eliminar_cliente(dni)   
                self.limpiarTabla()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Eliminar Cliente", "Debe seleccionar una fila...!!!", QtWidgets.QMessageBox.Ok)

    def modificar(self):

        if len(clientes.listar_clientes()) == 0:
            QtWidgets.QMessageBox.information(self, "Modificar Cliente", "No existen clientes a modificar...!!!", QtWidgets.QMessageBox.Ok)
        else:
            dni, _ = QtWidgets.QInputDialog.getText(self, "Modificar Cliente", "Ingrese el DNI a modificar")
            respuesta = clientes.consultar_clientes(dni)
            if len(respuesta) > 0:
                self.btnModificar.setVisible(False)
                self.btnGrabar.setVisible(True)
                self.txtDni.setText(dni)
                self.txtNombres.setText(respuesta[0][0])
                self.txtApellidoPaterno.setText(respuesta[0][0])
                self.txtApellidoMaterno.setText(respuesta[0][2])
                self.txtDireccion.setText(respuesta[0][3])
                self.txtTelefono.setText(respuesta[0][4])
        
    def grabar(self):

        try:
            datos = (self.obtenerNombres(), self.obtenerApellidoPaterno(), self.obtenerApellidoMaterno(), self.obtenerDireccion(), self.obtenerTelefono())
            respuesta = clientes.modificar_clientes(datos)
            self.btnModificar.setVisible(True)
            self.btnGrabar.setVisible(False)
            self.limpiarTabla()
            self.limpiarControles()
            self.listar()
        except:
            QtWidgets.QMessageBox.information(self, "Modificar Cliente", "Error al modificar cliente...!!!", QtWidgets.QMessageBox.Ok)