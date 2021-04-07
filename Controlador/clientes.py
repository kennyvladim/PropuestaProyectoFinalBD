class Cliente:

    def __init__(self, dniCliente, nombresCliente, apellidoPaternoCliente, apellidoMaternoCliente, direccionCliente, telefonoCliente):
        self.__dniCliente = dniCliente 
        self.__nombresCliente = nombresCliente
        self.__apellidoPaternoCliente = apellidoPaternoCliente
        self.__apellidoMaternoCliente = apellidoMaternoCliente
        self.__direccionCliente = direccionCliente
        self.__telefonoCliente = telefonoCliente
    
    def getDniCliente(self):
        return self.__dniCliente

    def getNombresCliente(self):
        return self.__nombresCliente

    def getApellidoPaternoCliente(self):
        return self.__apellidoPaternoCliente

    def getApellidoMaternoCliente(self):
        return self.__apellidoMaternoCliente

    def getDireccionCliente(self):
        return self.__direccionCliente

    def getTelefonoCliente(self):
        return self.__telefonoCliente

    def setDniCliente(self, dniCliente):
        self.__dniCliente = dniCliente

    def setNombresCliente(self, nombresCliente):
        self.__nombresCliente = nombresCliente
    
    def setApellidoPaternoCliente(self, apellidoPaternoCliente):
        self.__apellidoPaternoCliente = apellidoPaternoCliente

    def setApellidoMaternoCliente(self, apellidoMaternoCliente):
        self.__apellidoMaternoCliente = apellidoMaternoCliente

    def setDireccionCliente(self, direccionCliente):
        self.__direccionCliente = direccionCliente
    
    def setTelefonoCliente(self, telefonoCliente):
        self.__telefonoCliente = telefonoCliente