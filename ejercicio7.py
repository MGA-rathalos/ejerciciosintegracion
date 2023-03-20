from abc import ABC, abstractmethod

class Persona(ABC):

    def __init__(self,nombre=None):
        self.nombre = nombre

    def __str__(self):
        return f'{self.nombre}'

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
    


cuenta1 = Cuenta('Matias', 23000)
print(cuenta1.mostrar())


sumarsaldo = cuenta1.ingresar(2000)
print(sumarsaldo)