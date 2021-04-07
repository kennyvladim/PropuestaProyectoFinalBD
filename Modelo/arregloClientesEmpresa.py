from Controlador.clientesEmpresa import *

class ArregloClientes:

    def __init__(self):
        self.dataClientesEmpresa = []

    def adiciona(self, objCliEmp):
        self.dataClientesEmpresa.append(objCliEmp)

    def devolver(self, pos):
        return self.dataClientesEmpresa[pos]
    
    def tamaño(self):
        return len(self.dataClientesEmpresa)

    def buscar(self, ruc):
        for i in range(self.tamaño()):
            if ruc == self.dataClientesEmpresa[i].getRucCE():
                return i
        return -1

    def eliminar(self, indice):
        del(self.dataClientesEmpresa[indice])
    
