'''Cree una clase Vehículo que contenga los atributos de instancia velocidad_maxima y kilometraje.'''

class Vehiculo:
    def __init__(self, velocidad_maxima: int, kilometraje: int):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje