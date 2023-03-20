from abc import ABC, abstractmethod

class Persona(ABC):

    def __init__(self,nombre=None,edad=None,DNI=None):
        self.__nombre = nombre
        self.__edad = edad
        self.__DNI = DNI
       

    def __str__(self):
        return f'{self.__DNI}, {self.__nombre}, {self.__edad}'

    def mostrar(self):
        return f'Los datos de la persona son: {self.__nombre}, {self.__edad}, {self.__DNI}'
    
    def Es_mayor_de_edad(self):
        
        if self.__edad >= 18:
            return f'La persona es mayor de edad'
        else:
            return f'La persona es menor de edad'

###nombre
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre

##edad
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def nombre(self,nueva_edad):
        self.__edad = nueva_edad

persona_uno = Persona ('Pedro', 23, '33498706')
print(persona_uno.mostrar())
print(persona_uno.Es_mayor_de_edad())

persona_dos = Persona ('Ignacio', 12, '54633777')
print(persona_dos.mostrar())
print(persona_dos.Es_mayor_de_edad())