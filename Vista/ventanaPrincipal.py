from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui
from Vista.ventanaClientes import VentanaClientes
from Vista.ventanaDetalleVentas import VentanaDetalleVentas
from Vista.ventanaFacturas import VentanaFacturas
from Vista.ventanaProductos import VentanaProductos
from Vista.ventanaVentas import VentanaVentas

class VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(VentanaPrincipal,self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon("UI/imagenes/venta.png"))
        uic.loadUi("UI/ventanaPrincipal.ui",self)
        
        self.btnProductos.clicked.connect(self.abrirVentanaProductos)
        self.btnClientes.clicked.connect(self.abrirVentanaClientes)
        self.btnVender.clicked.connect(self.abrirVentanaVentas)
        self.btnDetalleVentas.clicked.connect(self.abrirVentanaDetalleVentas)
        self.btnVentas.clicked.connect(self.abrirVentanaFacturas)
        self.btnSalir.clicked.connect(self.cerrar)
        
    def abrirVentanaProductos(self):
        vproductos = VentanaProductos(self)
        vproductos.show()
    
    def abrirVentanaClientes(self):
        vclientes = VentanaClientes(self)
        vclientes.show()

    def abrirVentanaVentas(self):
        vVentas = VentanaVentas(self)
        vVentas.show()
    
    def abrirVentanaDetalleVentas(self):
        vDetalleVentas = VentanaDetalleVentas(self)
        vDetalleVentas.show()
    
    def abrirVentanaFacturas(self):
        vFacturas = VentanaFacturas(self)
        vFacturas.show()

    def cerrar(self):
        self.close()