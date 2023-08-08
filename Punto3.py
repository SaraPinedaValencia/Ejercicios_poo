'''A la clase del punto anterior, defínale los siguientes métodos:
- Un método mostrar que imprima por consola las coordenadas del punto
- Un método mover que cambie las coordenadas del punto
- Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto.'''

class Punto:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def mostrar(self):
        print(f'({self.x}, {self.y})')

    def mover(self, dx: float, dy: float):
        self.x += dx
        self.y += dy

    def calcular_distancia(self, otro_punto: 'Punto'):
        return ((self.x - otro_punto.x) ** 2 + (self.y - otro_punto.y) ** 2) ** 0.5