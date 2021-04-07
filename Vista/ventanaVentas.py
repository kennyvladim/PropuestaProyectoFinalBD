from datetime import date
from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui
from Controlador.factura import Factura
from Controlador.detalleVenta import DetalleVenta
from Modelo.arregloProductos import ArregloProductos
from Modelo.arregloClientes import ArregloClientes
from Modelo.arregloDetalleVenta import ArregloDetalleVenta
from Modelo.arregloFactura import ArregloFactura
from Vista.ventanaClientes import VentanaClientes
from Vista.ventanaProductos import VentanaProductos

aDetVent = ArregloDetalleVenta()
aFac = ArregloFactura() 
aCli = ArregloClientes()
aPro = ArregloProductos()

lista = []

class VentanaVentas(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(VentanaVentas,self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon("UI/imagenes/venta.png"))
        uic.loadUi("UI/ventanaVentas.ui", self)

        self.btnBuscarCliente.clicked.connect(self.buscarCliente)
        self.btnBuscarProducto.clicked.connect(self.buscarProducto)
        self.btnAgregar.clicked.connect(self.agregar)
        self.btnGenerar.clicked.connect(self.generarVenta)
        self.btnImprimirFactura.clicked.connect(self.imprimirFactura)
        self.btnCerrar.clicked.connect(self.cerrarVentana)
        self.calcularFecha()
        self.generarNumeroDocumento()
        self.item = 0
        self.stock_actual_temporal = {}

    def buscarCliente(self):
        codigoCliente = self.txtCodigoCliente.text()
        if self.txtCodigoCliente.text() == "":
            QtWidgets.QMessageBox.information(self, "Código Cliente", "Debe ingresar el código del cliente...!!!", QtWidgets.QMessageBox.Ok)
        else:
            pos = aCli.buscarCliente(codigoCliente)
            objCliente = aCli.devolverCliente(pos)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Código Cliente", "Cliente no registrado...!!!", QtWidgets.QMessageBox.Ok)
            else:
                self.txtNombres.setText(objCliente.getNombresCliente() + " " + objCliente.getApellidoPaternoCliente() + " " + objCliente.getApellidoMaternoCliente())
                   
    def buscarProducto(self):
        codigoProducto = self.txtCodigoProducto.text()
        if self.txtCodigoProducto.text() == "":
            QtWidgets.QMessageBox.information(self, "Código Producto", "Debe ingresar el código del producto...!!!", QtWidgets.QMessageBox.Ok)
        else:
            pos = aPro.buscarProducto(codigoProducto)
            objProducto = aPro.devolverProducto(pos)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Código Producto", "Producto no registrado...!!!", QtWidgets.QMessageBox.Ok)
            else:
                stock_temporal = self.obtenerStockActualTemporal(codigoProducto)
                if stock_temporal == -1:  # ocurre cuando no existe el producto en el diccionario
                    self.stock_actual_temporal[self.txtCodigoProducto.text()] = int(objProducto.getStockActual())
                    stock_temporal = self.obtenerStockActualTemporal(codigoProducto)  
                self.txtDescripcion.setText(objProducto.getDescripcion())
                self.txtStock.setText(str(stock_temporal))
                self.txtPrecio.setText(objProducto.getPrecioVenta())
    
    def obtenerStockActualTemporal(self, codigoProducto):
        stockEncontrado = -1 # variable auxiliar que contiene de manera predeterminada -1, indicando que no se encontró el stock
        if len(self.stock_actual_temporal) != 0: 
            for llave in self.stock_actual_temporal:
                if llave == codigoProducto:
                    stockEncontrado = self.stock_actual_temporal[llave]
                    return stockEncontrado
        return stockEncontrado

    def actualizarStockActualTemporal(self, codigoProducto, cantidad):
        for llave in self.stock_actual_temporal:
            if llave == codigoProducto:
                self.stock_actual_temporal[llave]= self.stock_actual_temporal[llave] - cantidad

    def obtenerNumeroDocumento(self):
        return self.txtNumeroDocumento.text()
    
    def obtenerCodigo(self):
        return self.txtCodigoProducto.text()
    
    def obtenerDescripcion(self):
        return self.txtDescripcion.text()
    
    def obtenerPrecio(self):
        return float(self.txtPrecio.text())

    def obtenerCantidad(self):
        return int(self.txtCantidad.text())  
    
    def obtenerItem(self):
        self.item = self.item + 1
        return self.item
    
    def obtenerFecha(self):
        return self.txtFecha.text() 

    def calcularFecha(self):
        self.fecha = date.today()
        dia = self.fecha.day
        mes = self.fecha.month
        año = self.fecha.year
        self.txtFecha.setText(str(dia) + "/" + str(mes) + "/" + str(año))

    def imprimirFactura(self):
        try:
            if self.txtNumeroDocumento.text() == "":
                QtWidgets.QMessageBox.information(self, "Imprimir Factura", "No se ha realizado ninguna venta...!!!", QtWidgets.QMessageBox.Ok)    
            else:                
                numeroFactura = self.txtNumeroDocumento.text()
                pos = aFac.buscarFactura(numeroFactura)
                objFact = aFac.devolverFactura(pos)
                codigoCliente = self.txtCodigoCliente.text()
                pos = aCli.buscarCliente(codigoCliente)
                objCliente = aCli.devolverCliente(pos)
                objFact.imprimirDocumentoVenta(objCliente)
                aDetVent.imprimirDetalleVenta(numeroFactura, aPro)
                QtWidgets.QMessageBox.information(self, "Imprimir Factura", "La factura se ha impreso correctamente...!!!", QtWidgets.QMessageBox.Ok) 
                self.close()
        except:
            QtWidgets.QMessageBox.information(self, "Imprimir Factura", "No se ha realizado ninguna venta...!!!", QtWidgets.QMessageBox.Ok)    

    def agregar(self):
        try:
            if int(self.txtCantidad.text()) > int(self.txtStock.text()):
                QtWidgets.QMessageBox.information(self, "Venta", "No se puede vender esa cantidad...!!!", QtWidgets.QMessageBox.Ok)
            elif int(self.txtCantidad.text()) <= 0:
                QtWidgets.QMessageBox.information(self, "Venta", "La cantidad ingresada es incorrecta...!!!", QtWidgets.QMessageBox.Ok)
            else:
                lista.append((self.obtenerItem(), self.obtenerCodigo(), self.obtenerDescripcion(), self.obtenerPrecio(), self.obtenerCantidad(),self.obtenerPrecio()*self.obtenerCantidad()))
                self.actualizarStockActualTemporal(self.obtenerCodigo(),self.obtenerCantidad())
                self.mostrarDetalle()                 
                self.calcularPago()
        except:
            QtWidgets.QMessageBox.information(self, "Agregar Detalle", "No se ha completado los detalles del producto...!!!", QtWidgets.QMessageBox.Ok) 
            self.item = self.item - 1

    def mostrarDetalle(self):
        self.tblDetalle.setRowCount(len(lista))
        self.tblDetalle.setColumnCount(6)
        self.tblDetalle.verticalHeader().setVisible(False)
        for i in range(len(lista)):
            self.tblDetalle.setItem(i, 0, QtWidgets.QTableWidgetItem(str(lista[i][0])))
            self.tblDetalle.setItem(i, 1, QtWidgets.QTableWidgetItem(str(lista[i][1])))
            self.tblDetalle.setItem(i, 2, QtWidgets.QTableWidgetItem(str(lista[i][2])))
            self.tblDetalle.setItem(i, 3, QtWidgets.QTableWidgetItem(str(lista[i][3])))
            self.tblDetalle.setItem(i, 4, QtWidgets.QTableWidgetItem(str(lista[i][4])))
            self.tblDetalle.setItem(i, 5, QtWidgets.QTableWidgetItem(str(lista[i][5])))
        self.limpiarControles()

    def limpiarControles(self):
        self.txtCodigoProducto.clear()
        self.txtDescripcion.clear()
        self.txtStock.clear()
        self.txtPrecio.clear()
        self.txtCantidad.clear()
    
    def limpiarControlesTotal(self):
        self.txtNumeroDocumento.clear()
        self.txtCodigoCliente.clear()
        self.txtNombres.clear()
        self.txtCodigoProducto.clear()
        self.txtDescripcion.clear()
        self.txtStock.clear()
        self.txtPrecio.clear()
        self.txtCantidad.clear()
        self.txtTotalPagar.clear()
        self.tblDetalle.clearContents()
        self.tblDetalle.setRowCount(0)

    def calcularPago(self):
        self.subtotal_pagar = 0
        for i in range(len(lista)):
            self.subTotal = lista[i][5]
            self.subtotal_pagar = self.subtotal_pagar + float(self.subTotal)
            self.igv = 0.18 * self.subtotal_pagar
            self.total_pagar = self.subtotal_pagar + self.igv 
        self.txtSubTotal.setText("S/. " + str(round(self.subtotal_pagar, 2)))
        self.txtIgv.setText("S/. " + str(round(self.igv, 2)))
        self.txtTotalPagar.setText("S/. " + str(round(self.total_pagar, 2)))

    def generarVenta(self):
        if self.tblDetalle.rowCount() == 0:
            QtWidgets.QMessageBox.information(self, "Venta", "No se ha agregado ningún detalle...!!!", QtWidgets.QMessageBox.Ok)
        else: 
            objFact = Factura(self.obtenerNumeroDocumento(), self.obtenerFecha(), self.txtIgv.text(), self.txtTotalPagar.text(), self.txtCodigoCliente.text())
            numeroFactura = self.obtenerNumeroDocumento()
            if aFac.buscarFactura(numeroFactura) == -1:
                aFac.adicionaFactura(objFact)
                self.actualizarStock()
                self.guardarDetalleVenta()
                aFac.grabar()
                aPro.grabar()
                QtWidgets.QMessageBox.information(self, "Venta", "Se realizó la venta correctamente...!!!", QtWidgets.QMessageBox.Ok)
                lista.clear()
            else:
                QtWidgets.QMessageBox.information(self, "Venta", "El número de factura ingesado ya existe...!!!", QtWidgets.QMessageBox.Ok)

    def actualizarStock(self):
        for i in range(self.tblDetalle.rowCount()):
            codigoProducto = self.tblDetalle.item(i, 1).text()
            cantidad = int(self.tblDetalle.item(i, 4).text())
            pos = aPro.buscarProducto(codigoProducto)
            objProducto = aPro.devolverProducto(pos)
            stock_actual = int(objProducto.getStockActual()) - cantidad
            aPro.actualizarStock(stock_actual, codigoProducto)

    def guardarDetalleVenta(self):
        for i in range(len(lista)):
            objDetVent = DetalleVenta(self.obtenerNumeroDocumento(), lista[i][0], lista[i][1], lista[i][3], lista[i][4])
            aDetVent.adicionaDetalleVenta(objDetVent)
            aDetVent.grabar()

    def generarNumeroDocumento(self):
        numeroDocunento = aFac.nroSerie()
        if numeroDocunento == 0:
            self.txtNumeroDocumento.setText("000001")
        else:
            self.incremento = numeroDocunento
            self.incremento = self.incremento + 1
            self.txtNumeroDocumento.setText("00000" + str(self.incremento))

    def cerrarVentana(self):
        lista.clear()
        self.close()