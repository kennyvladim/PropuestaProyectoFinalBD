from Controlador.detalleVenta import DetalleVenta

class ArregloDetalleVenta:

    def __init__(self):
        self.dataDetalleVenta = []
        self.cargar()
    
    def cargar(self):
        archivo = open("Modelo/DetalleVenta.txt", "r", encoding = "utf-8")
        for linea in archivo.readlines():
            columna = str(linea).split(",")
            numero_documento = columna[0]
            numero_item = columna[1]
            codigo_producto = columna[2]
            precio_venta = columna[3]
            cantidad = columna[4].strip()
            objDetVent = DetalleVenta(numero_documento, numero_item, codigo_producto, precio_venta, cantidad)
            self.adicionaDetalleVenta(objDetVent)
        archivo.close()

    def grabar(self):
        archivo = open("Modelo/DetalleVenta.txt", "w+", encoding = "utf-8")
        for i in range(self.tamañoDetalleVenta()):
            archivo.write(str(self.devolverDetalleVenta(i).getNDocumentoVenta()) + "," 
            + str(self.devolverDetalleVenta(i).getNItem()) + ","
            + str(self.devolverDetalleVenta(i).getCodigoProducto()) + ","
            + str(self.devolverDetalleVenta(i).getPrecioVenta()) + ","
            + str(self.devolverDetalleVenta(i).getCantidad()) + "\n")
        archivo.close()

    def adicionaDetalleVenta(self, objDetVent):
        self.dataDetalleVenta.append(objDetVent)

    def devolverDetalleVenta(self, pos):
        return self.dataDetalleVenta[pos]
    
    def tamañoDetalleVenta(self):
        return len(self.dataDetalleVenta)

    def buscarDetalleVenta(self, nDocumentoVenta):
        for i in range(self.tamañoDetalleVenta()):
            if nDocumentoVenta == self.dataDetalleVenta[i].getNDocumentoVenta:
                return i
        return -1

    def eliminarDetalleVenta(self, indice):
        del(self.dataDetalleVenta[indice])
    
    def imprimirDetalleVenta(self, nDocumentoVenta, aPro):
        for objDetVent in self.dataDetalleVenta:
            if objDetVent.getNDocumentoVenta() == nDocumentoVenta:
                pos = aPro.buscarProducto(objDetVent.getCodigoProducto())  
                objPro = aPro.devolverProducto(pos)
                objDetVent.imprimirLineaDetalleVenta(objPro)

    