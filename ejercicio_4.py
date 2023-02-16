import math
class Rectangulo:
    def __init__(self, x_esquina_1: int, y_esquina_1: int, x_esquina_2: int, y_esquina_2: int):
        self.x_esquina_1 = x_esquina_1
        self.y_esquina_1 = y_esquina_1
        self.x_esquina_2 = x_esquina_2
        self.y_esquina_2 = y_esquina_2

    def calcular_distancia(self) -> float:
        return math.sqrt((self.x_esquina_2-self.x_esquina_1)**2+(self.y_esquina_2-self.y_esquina_1)**2)

    def calcular_lados(self) -> float:
        return ((self.calcular_distancia() ** 2) / 2) ** 1/2









