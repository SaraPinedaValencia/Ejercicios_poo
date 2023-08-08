'''Cree una clase Circulo que tenga las propiedades centro y radio, 
las cuales se inicializan con parámetros en el constructor. 
Defina métodos en la clase para calcular el área, el perímetro e indicar si un punto pertenece al círculo o no.'''
from Punto3 import Punto

class Circulo:
    def __init__(self, centro: 'Punto', radio: float):
        self.centro = centro
        self.radio = radio

    def calcular_area(self):
        return 3.14 * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * 3.14 * self.radio

    def punto_pertenece(self, punto: 'Punto'):
        distancia_centro_punto = self.centro.calcular_distancia(punto)
        return distancia_centro_punto <= self.radio