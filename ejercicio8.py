from abc import ABC, abstractmethod

class Persona(ABC):

    def __init__(self,nombre=None,edad=None,DNI=None):
        self.__nombre = nombre
        self.edad = edad
        self.__DNI = DNI
     
    def __str__(self):
        return f'{self.__DNI}, {self.__nombre}, {self.edad}'

class Titular(Persona):

    def __init__(self,nombre=None):
        super().__init__(nombre)
    
    def __str__(self):
        return f'{self.nombre}'
    
    @property
    def titular(self):
        return self.titular
    

class Cuenta(Titular):

    def __init__(self, nombre=None, cantidad=float):
        super().__init__(nombre)
        self.cantidad = cantidad
       
    def __str__(self, cantidad):
        return f'{self.nombre}, {self.cantidad}'
    
    
    def mostrar(self):
        return f'La cuenta del titular es de: {self.nombre}, y contiene {self.cantidad} pesos'
    
    def ingresar(cantidad):
        saldo = saldo + cantidad
        return True, saldo
    
    def retirar(cantidad):
        saldo = cantidad - saldo
        return True, saldo

    @property
    def cantidad(self):
        return self.cantidad
    
class Cuenta_Joven(Cuenta):

    def __init__(self, nombre=None, cantidad=float, bonificacion):
        super().__init__(nombre, cantidad)
        self.bonificacion = bonificacion

    def __str__(self, cantidad):
        return f'{self.nombre}, {self.cantidad}'
    
    def es_titular_valido(self):
        if self.edad >= 18 AND < 25:
            return f'La persona es mayor de edad'
        else:
            return f'La persona es menor de edad'

    def ingresar(cantidad):
        saldo = saldo + cantidad
        return True, saldo
        
    def retirar(cantidad):
        if self.edad >= 18 AND < 25:
            saldo = cantidad - saldo
            return True, saldo
        else:
            return f'La persona no tiene permitida la operacion'
        
    def mostrar(self):
        return f'La Cuenta Joven del titular: {self.nombre}, y contiene {self.cantidad} pesos y una bonificacion de {self.bonificacion}'
    
    @property
    def cantidad(self):
        return self.cantidad