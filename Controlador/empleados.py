class Empleado:

    def __init__(self, dniEmpleado, nombresEmpleado, apellidoPaternoEmpleado, apellidoMaternoEmpleado, direccionEmpleado, telefonoEmpleado):
        self.__dniEmpleado = dniEmpleado 
        self.__nombresEmpleado = nombresEmpleado
        self.__apellidoPaternoEmpleado = apellidoPaternoEmpleado
        self.__apellidoMaternoEmpleado = apellidoMaternoEmpleado
        self.__direccionEmpleado = direccionEmpleado
        self.__telefonoEmpleado = telefonoEmpleado
    
    def getDniEmpleado(self):
        return self.__dniEmpleado

    def getNombresEmpleado(self):
        return self.__nombresEmpleado

    def getApellidoPaternoEmpleado(self):
        return self.__apellidoPaternoEmpleado

    def getApellidoMaternoEmpleado(self):
        return self.__apellidoMaternoEmpleado

    def getDireccionEmpleado(self):
        return self.__direccionEmpleado

    def getTelefonoEmpleado(self):
        return self.__telefonoEmpleado

    def setDniEmpleado(self, dniEmpleado):
        self.__dniEmpleado = dniEmpleado

    def setNombresEmpleado(self, nombresEmpleado):
        self.__nombresEmpleado = nombresEmpleado
    
    def setApellidoPaternoEmpleado(self, apellidoPaternoEmpleado):
        self.__apellidoPaternoEmpleado = apellidoPaternoEmpleado

    def setApellidoMaternoEmpleado(self, apellidoMaternoEmpleado):
        self.__apellidoMaternoEmpleado = apellidoMaternoEmpleado

    def setDireccionEmpleado(self, direccionEmpleado):
        self.__direccionEmpleado = direccionEmpleado
    
    def setTelefonoEmpleado(self, telefonoEmpleado):
        self.__telefonoEmpleado = telefonoEmpleado