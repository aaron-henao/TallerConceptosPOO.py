import math
import random


class Punto:

    def __init__(self, x: int, y: int):

        self.x = x
        self.y = y
        self.x2 = random(-100, 100)
        self.y2 = random(-100, 100)

    def mostrar(self):
        return self.x, self.y

    def mover(self):
        return self.x2, self.y2

    def calcular_distancia(self) -> float:
        return math.sqrt((self.x2-self.x)**2+(self.y2-self.y)**2)














