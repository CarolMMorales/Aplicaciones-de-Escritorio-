class ComunidadUniempresarial():
    #constructor
    def __init__(self, nombre, apellido, cargo):
        #atributos
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cargo = cargo
    #metodo/comportamiento
    def imprimirIntegrante(self):
        nombres = self.__nombre + " " + self.__apellido
        return f"Nombres: {nombres} - Cargo: {self.__cargo}"
