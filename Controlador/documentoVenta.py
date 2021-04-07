class DocumentoVenta:

    def __init__(self, nDocumentoVenta, fecha, igv, totalPrecioVenta):
        self.__nDocumentoVenta = nDocumentoVenta
        self.__fecha = fecha
        self.__igv = igv
        self.__totalPrecioVenta = totalPrecioVenta
        self.__estado = "Vigente" 
    
    def getNDocumentoVenta(self):
        return self.__nDocumentoVenta

    def getFecha(self):
        return self.__fecha

    def getIgv(self):
        return self.__igv

    def getTotalPrecioVenta(self):
        return self.__totalPrecioVenta
    
    def setNDocumentoVenta(self, nDocumentoVenta):
        self.__nDocumentoVenta = nDocumentoVenta

    def setFecha(self, fecha):
        self.__fecha = fecha

    def setIgv(self, igv):
        self.__igv = igv
        
    def setTotalPrecioVenta(self, totalPrecioVenta):
        self.__totalPrecioVenta = totalPrecioVenta
    
    def getEstado(self):
        return self.__estado
    
    def setEstado(self, estado):
        self.__estado = estado
    
    def imprimirDocumentoVenta(self):
        print("")
        print("")
        print("******************************")
        print("***** DOCUMENTO DE VENTA *****")
        print("******************************")
        print("N° DOCUMENTO DE VENTA\t: ", self.__nDocumentoVenta)
        print("FECHA\t\t\t: ", self.__fecha)
        print("IGV\t\t\t: ", self.__igv)
        print("TOTAL A PAGAR\t\t: ", self.__totalPrecioVenta)
        print("ESTADO\t\t\t: ", self.__estado)
 
    
    