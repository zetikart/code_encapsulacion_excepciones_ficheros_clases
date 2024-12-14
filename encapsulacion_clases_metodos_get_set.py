
# encapsulacion se usa para ocultar los detalles internos de un objeto y proporcionar una interfaz publica para interactuar con el.

# es el iniciador
class Persona:
    def __init__(self, nombre, edad, direccion):
        self.__nombre = nombre
        self.__edad = edad
        self.__direccion = direccion

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

    def get_direccion(self):
        return self.__direccion

    def set_direccion(self, direccion):
        self.__direccion = direccion

# privados utilizando doble guión bajo (__)
# metodos get set publicos publicos para acceder y modificar
# set se usa para establecer los valores de los atributos
# get se utilizan para obtener los valores de los atributos
        

persona = Persona("Juan", 25, "Calle 123")
nombre = persona.get_nombre()
edad = persona.get_edad()
print(nombre, edad)
