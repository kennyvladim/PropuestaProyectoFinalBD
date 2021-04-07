class ClienteEmpresa:

    def __init__(self, rucCE, razonSocialCE, direccionCE, telefonoCE):
        self.__rucCE = rucCE 
        self.__razonSocialCE = razonSocialCE
        self.__direccionCE= direccionCE
        self.__telefonoCE = telefonoCE
    
    def getRucCE(self):
        return self.__rucCE

    def getRazonSocialCE(self):
        return self.__razonSocialCE

    def getDireccionCE(self):
        return self.__direccionCE

    def getTelefonoCE(self):
        return self.__telefonoCE

    def setRucCe(self, rucCE):
        self.__rucCE = rucCE

    def setRazonSocialCE(self, razonSocialCE):
        self.__razonSocialCE = razonSocialCE

    def setDireccionCE(self, direccionCE):
        self.__direccionCE = direccionCE

    def setTelefonoCE(self, telefonoCE):
        self.__telefonoCE = telefonoCE
