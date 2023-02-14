import math


class Punto:

    def __init__(self, x: int, y: int, x2: int, y2: int):

        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2

    def mostrar(self):
        return self.x, self.y

    def mover(self):
        return self.x2, self.y2

    def calcular_distancia(self, distancia: float):
        self.distancia = math.sqrt((self.x2-self.x)**2+(self.y2-self.y)**2)
        return distancia













