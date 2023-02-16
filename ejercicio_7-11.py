class CuentaBancaria:

    def __init__(self, numero_cuenta: int, propietarios: str, balance: float):

        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self):
        return

    def retirar(self):
        return

    def aplicar_cuota_manejo(self) -> float:
        return self.balance * (2/100) + self.balance

    def mostrar_detalles(self):
        print(self.propietarios())
        print(self.numero_cuenta())
        print(self.balance())
        print(self.aplicar_cuota_manejo())

