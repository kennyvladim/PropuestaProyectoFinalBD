from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui
from Modelo.arregloFactura import ArregloFactura

class VentanaFacturas(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(VentanaFacturas,self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon("UI/imagenes/venta.png"))
        uic.loadUi("UI/ventanaFactura.ui", self)
    
        self.btnMostrar.clicked.connect(self.listar)

    def listar(self):
        aFac = ArregloFactura()
        self.tblFactura.setRowCount(aFac.tamañoFactura())
        self.tblFactura.setColumnCount(6)
        self.tblFactura.verticalHeader().setVisible(False)
        for i in range(0, aFac.tamañoFactura()):
            self.tblFactura.setItem(i, 0, QtWidgets.QTableWidgetItem(aFac.devolverFactura(i).getNDocumentoVenta()))
            self.tblFactura.setItem(i, 1, QtWidgets.QTableWidgetItem(aFac.devolverFactura(i).getFecha()))
            self.tblFactura.setItem(i, 2, QtWidgets.QTableWidgetItem(aFac.devolverFactura(i).getIgv()))
            self.tblFactura.setItem(i, 3, QtWidgets.QTableWidgetItem(aFac.devolverFactura(i).getTotalPrecioVenta()))
            self.tblFactura.setItem(i, 4, QtWidgets.QTableWidgetItem(aFac.devolverFactura(i).getRuc()))
            self.tblFactura.setItem(i, 5, QtWidgets.QTableWidgetItem(aFac.devolverFactura(i).getEstado()))
            

