from Controlador.factura import Factura

class ArregloFactura:

    def __init__(self):
        self.dataFactura = []
        self.cargar()
    
    def cargar(self):
        archivo = open("Modelo/Factura.txt", "r", encoding = "utf-8")
        for linea in archivo.readlines():
            columna = str(linea).split(",")
            numero_documento = columna[0]
            fecha = columna[1]
            igv = columna[2]
            total_precio_venta = columna[3]
            dni = columna[4].strip()
            objFact = Factura(numero_documento, fecha, igv, total_precio_venta, dni)
            self.adicionaFactura(objFact)
        archivo.close()

    def grabar(self):
        archivo = open("Modelo/Factura.txt", "w+", encoding = "utf-8")
        for i in range(self.tamañoFactura()):
            archivo.write(str(self.devolverFactura(i).getNDocumentoVenta()) + "," 
            + str(self.devolverFactura(i).getFecha()) + ","
            + str(self.devolverFactura(i).getIgv()) + ","
            + str(self.devolverFactura(i).getTotalPrecioVenta()) + ","
            + str(self.devolverFactura(i).getRuc()) + ","
            + str(self.devolverFactura(i).getEstado()) + "\n")
        archivo.close()

    def adicionaFactura(self, objFact):
        self.dataFactura.append(objFact)

    def devolverFactura(self, pos):
        return self.dataFactura[pos]
    
    def tamañoFactura(self):
        return len(self.dataFactura)

    def buscarFactura(self, nDocumentoVenta):
        for i in range(self.tamañoFactura()):
            if nDocumentoVenta == self.dataFactura[i].getNDocumentoVenta():
                return i
        return -1

    def eliminarFactura(self, indice):
        del(self.dataFactura[indice])
    
    def nroSerie(self):
        self.series = []
        for i in range(self.tamañoFactura()):
            self.series.append(self.dataFactura[i].getNDocumentoVenta())
        return len(self.series)
    



    
 

    


