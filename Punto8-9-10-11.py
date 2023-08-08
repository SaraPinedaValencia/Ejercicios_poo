'''Para la clase CuentaBancaria, cree un método depositar que maneje las acciones de depósito en la cuenta.
Para la clase CuentaBancaria, cree un método retirar que maneje las acciones de retiro de la cuenta.
Para la clase CuentaBancaria, cree un método aplicar_cuota_manejo que aplique un porcentaje del 2% sobre el balance de la cuenta
Para la clase CuentaBancaria, cree un método mostrar_detalles que imprima por consola los detalles de la cuenta bancaria.
'''
class CuentaBancaria:
    def __init__(self, numero_cuenta: str, propietarios: str, balance: float):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, monto: float):
        self.balance += monto

    def retirar(self, monto: float):
        if monto > self.balance:
            print('Fondos insuficientes')
            return False
        else:
            self.balance -= monto
            return True

    def aplicar_cuota_manejo(self):
        cuota_manejo = 0.02 * self.balance
        self.balance -= cuota_manejo

    def mostrar_detalles(self):
        print(f'Número de cuenta: {self.numero_cuenta}')
        print(f'Propietarios: {self.propietarios}')
        print(f'Balance: {self.balance}')
