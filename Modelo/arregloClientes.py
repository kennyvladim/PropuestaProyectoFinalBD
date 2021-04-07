from Controlador.clientes import Cliente

class ArregloClientes:

    def __init__(self):
        self.dataClientes = []
        self.cargar() 
       
    def cargar(self):
        archivo = open("Modelo/Clientes.txt", "r", encoding = "utf-8")
        for linea in archivo.readlines():
            columna = str(linea).split(",")
            dni = columna[0]
            nombres = columna[1]
            apellido_paterno = columna[2]
            apellido_materno = columna[3]
            direccion = columna[4]
            telefono = columna[5].strip()
            objCli = Cliente(dni, nombres, apellido_paterno, apellido_materno, direccion, telefono)
            self.adicionaCliente(objCli)
        archivo.close()

    def grabar(self):
        archivo = open("Modelo/Clientes.txt", "w+", encoding = "utf-8")
        for i in range(self.tamañoArregloCliente()):
            archivo.write(str(self.devolverCliente(i).getDniCliente()) + "," 
            + str(self.devolverCliente(i).getNombresCliente()) + "," 
            + str(self.devolverCliente(i).getApellidoPaternoCliente()) + ","
            + str(self.devolverCliente(i).getApellidoMaternoCliente()) + ","
            + str(self.devolverCliente(i).getDireccionCliente()) + ","
            + str(self.devolverCliente(i).getTelefonoCliente()) + "\n")
        archivo.close()

    def adicionaCliente(self, objCli):
        self.dataClientes.append(objCli)

    def devolverCliente(self, pos):
        return self.dataClientes[pos]
    
    def tamañoArregloCliente(self):
        return len(self.dataClientes)

    def buscarCliente(self, dni):
        for i in range(self.tamañoArregloCliente()):
            if dni == self.dataClientes[i].getDniCliente():
                return i
        return -1

    def eliminarCliente(self, indice):
        del(self.dataClientes[indice])
    


    
    
    
    


    


