class Informatico:
    def __init__(self, nombre, apellidos, edad, casado, especialidad):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__edad = edad
        self.__casado = casado
        self.__especialidad = especialidad

    def setNombre(self, nombre):
        self.__nombre = nombre
    def getNombre(self):
        return self.__nombre

    def setApellidos(self, apellidos):
        self.__apellidos = apellidos
    def getApellidos(self):
        return self.__apellidos

    def setEdad(self, edad):
        self.__edad = edad
    def getEdad(self):
        return self.__edad

    def setCasado(self, casado):
        self.__casado = casado
    def getCasado(self):
        return self.__casado

    def setEspecialidad(self, especialidad):
        self.__especialidad = especialidad
    def getEspecialidad(self):
        return self.__especialidad
    
    def __str__(self):
        return  "Nombre: {}\n" \
                "Apellidos: {}\n" \
                "Edad: {}\n" \
                "Casado: {}\n" \
                "Especialidad: {}\n" \
                .format(self.__nombre, self.__apellidos, self.__edad, self.__casado, self.__especialidad)
    
