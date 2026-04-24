class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    def imprimir(self):
        print("Titular:", self.titular)
        print("Cantidad:", self.cantidad)


class CajaAhorro(Cuenta):
    def __init__(self, titular, cantidad):
        super().__init__(titular, cantidad)

    def mostrar_informacion(self):
        print("Información Caja de Ahorro")
        self.imprimir()


class PlazoFijo(Cuenta):
    def __init__(self, titular, cantidad, plazo, interes):
        super().__init__(titular, cantidad)
        self.plazo = plazo
        self.interes = interes

    def importe_interes(self):
        importe = (self.cantidad * self.interes) / 100
        return importe

    def mostrar_informacion(self):
        print("Información Plazo Fijo")
        self.imprimir()
        print("Plazo en días:", self.plazo)
        print("Interés:", self.interes, "%")
        print("Total de interés acumulado:", self.importe_interes())


caja = CajaAhorro("Lucía Pérez", 1500)
caja.mostrar_informacion()

print("") 

plazo = PlazoFijo("Carlos Ruiz", 5000, 30, 5.5)
plazo.mostrar_informacion()