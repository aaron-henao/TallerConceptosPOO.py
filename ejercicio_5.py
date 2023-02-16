import math


class Circulo:
    def __init__(self, x_punto_1: int, y_punto_1: int, radio: float, x_punto_2: int, y_punto_2: int):
        self.x_punto_1 = x_punto_1
        self.y_punto_1 = y_punto_1
        self.x_punto_2 = x_punto_2
        self.y_punto_2 = y_punto_2
        self.radio = radio

    def calcular_area(self) -> float:
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def distancia(self) -> float:
        return ((self.x_punto_2 - self.x_punto_1) ** 2 + (self.y_punto_2 - self.y_punto_1) ** 2)**1/2

    def pertenece(self):
        if self.distancia() < self.radio:
            return True
        else:
            return False







