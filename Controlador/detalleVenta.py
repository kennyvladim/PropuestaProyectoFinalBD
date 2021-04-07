class DetalleVenta:

    def __init__(self, nDocumentoVenta, nItem, codigoProducto, precioVenta, cantidad):
        self.__nDocumentoVenta = nDocumentoVenta 
        self.__nItem = nItem
        self.__codigoProducto = codigoProducto
        self.__precioVenta = precioVenta
        self.__cantidad = cantidad
            
    def getNDocumentoVenta(self):
        return self.__nDocumentoVenta

    def getNItem(self):
        return self.__nItem

    def getCodigoProducto(self):
        return self.__codigoProducto
 
    def getPrecioVenta(self):
        return self.__precioVenta

    def getCantidad(self):
        return self.__cantidad

    def setNDocumentoVenta(self, nDocumentoVenta):
        self.__nDocumentoVenta = nDocumentoVenta

    def setNItem(self, nItem):
        self.__nItem = nItem
    
    def setCodigoProducto(self, codigoProducto):
        self.__codigoProducto = codigoProducto

    def setPrecioVenta(self, precioVenta):
        self.__precioVenta = precioVenta

    def setCantidad(self, cantidad):
        self.__cantidad = cantidad

    def imprimirLineaDetalleVenta(self, objPro):
        print("")
        print(self.__nItem, "\t", self.__codigoProducto, "\t\t\t", objPro.getDescripcion(), "\t\t", self.__precioVenta, "\t\t", self.__cantidad)
        