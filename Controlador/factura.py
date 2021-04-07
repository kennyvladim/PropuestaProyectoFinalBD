from Controlador.documentoVenta import DocumentoVenta

class Factura(DocumentoVenta):

    def __init__(self, nDocumentoVenta, fecha, igv, totalPrecioVenta, dni):
        super().__init__(nDocumentoVenta, fecha, igv, totalPrecioVenta)
        self.__dni = dni

    def getRuc(self):
        return self.__dni
        
    def setRuc(self, dni):
        self.__dni = dni

    def imprimirDocumentoVenta(self, objCli):
        super().imprimirDocumentoVenta()
        print("")
        print("---------------------")
        print("| DATOS DEL CLIENTE |")
        print("---------------------")
        print("DNI\t\t\t: ", self.__dni)
        print("NOMBRES Y APELLIDOS\t: ", objCli.getNombresCliente(), objCli.getApellidoPaternoCliente(), objCli.getApellidoMaternoCliente())
        print("DIRECCIÓN\t\t: ", objCli.getDireccionCliente())
        print("")
        print("--------------------")
        print("| DETALLE DE VENTA |")
        print("--------------------") 
        print("")
        print("ITEM\t", "CÓDIGO DE PRODUCTO\t", "DESCRIPCION\t\t", "PRECIO DE VENTA\t", "CANTIDAD")
        print("----\t", "------------------\t", "-----------\t\t", "---------------\t", "--------")       





    

    

    
        
