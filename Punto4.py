'''Cree una clase Rectángulo la cual contiene dos atributos de instancia que representan los puntos que definen 
sus esquinas. Agregue métodos a la clase Rectángulo para calcular su perímetro, 
calcular su área e indicar si el rectángulo es un cuadrado.'''

from Punto3 import Punto

class Rectangulo:
    def __init__(self, esquina1: 'Punto', esquina2: 'Punto'):
        self.esquina1 = esquina1
        self.esquina2 = esquina2

    def calcular_perimetro(self):
        lado1 = abs(self.esquina1.x - self.esquina2.x)
        lado2 = abs(self.esquina1.y - self.esquina2.y)
        return 2 * (lado1 + lado2)

    def calcular_area(self):
        lado1 = abs(self.esquina1.x - self.esquina2.x)
        lado2 = abs(self.esquina1.y - self.esquina2.y)
        return lado1 * lado2

    def es_cuadrado(self):
        lado1 = abs(self.esquina1.x - self.esquina2.x)
        lado2 = abs(self.esquina1.y - self.esquina2.y)
        return lado1 == lado2