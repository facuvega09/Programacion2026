class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cantidad = 0

    def depositar(self, monto):
        self.cantidad = self.cantidad + monto

    def extraer(self, monto):
        self.cantidad = self.cantidad - monto

    def mostrar_total(self):
        print("El cliente", self.nombre, "tiene un total de:", self.cantidad)

class Banco:
    def __init__(self):
        self.cliente1 = Cliente("Juan")
        self.cliente2 = Cliente("Ana")
        self.cliente3 = Cliente("Pedro")

    def operar(self):
        self.cliente1.depositar(1000)
        self.cliente2.depositar(500)
        self.cliente3.depositar(2000)
        self.cliente1.extraer(200)

    def deposito_total(self):
        total = self.cliente1.cantidad + self.cliente2.cantidad + self.cliente3.cantidad
        print("--- Resumen de saldos ---")
        self.cliente1.mostrar_total()
        self.cliente2.mostrar_total()
        self.cliente3.mostrar_total()
        print("El total de dinero en el banco es:", total)

mi_banco = Banco()
mi_banco.operar()
mi_banco.deposito_total()