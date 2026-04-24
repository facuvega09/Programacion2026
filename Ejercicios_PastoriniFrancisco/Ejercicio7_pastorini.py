
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
        print("")
        print("INFORMACION CAJA DE AHORRO")
        self.imprimir()




class PlazoFijo(Cuenta):
    def __init__(self, titular, cantidad, plazo, interes):
        super().__init__(titular, cantidad)
        self.plazo = plazo
        self.interes = interes

    def obtener_importe_interes(self):
        importe = self.cantidad * self.interes / 100
        return importe

    def mostrar_informacion(self):
        print("INFORMACION PLAZO FIJO")
        self.imprimir()
        print("Plazo:", self.plazo)
        print("Interes %:", self.interes)
        print("Total de interes:", self.obtener_importe_interes())


caja = CajaAhorro("Juan Perez", 5000)
caja.mostrar_informacion()
print("")

plazo = PlazoFijo("Ana Gomez", 10000, 30, 0.75)
plazo.mostrar_informacion()
print("")