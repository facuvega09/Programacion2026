class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cantidad = 0

    def depositar(self, monto):
        self.cantidad = self.cantidad + monto

    def extraer(self, monto):
        self.cantidad = self.cantidad - monto

    def mostrar_total(self):
        print(self.nombre, "tiene:", self.cantidad)




class Banco:
    def __init__(self):
        print("--- REGISTRO DE CLIENTES ---")
        nom1 = input("Nombre del primer cliente: ")
        self.cliente1 = Cliente(nom1)
        
        nom2 = input("Nombre del segundo cliente: ")
        self.cliente2 = Cliente(nom2)
        
        nom3 = input("Nombre del tercer cliente: ")
        self.cliente3 = Cliente(nom3)

    def operar(self):
        print("")
        print(" OPERACIONES")
        print("1.", self.cliente1.nombre)
        print("2.", self.cliente2.nombre)
        print("3.", self.cliente3.nombre)
        opcion = input("Que cliente sos: ")
        

        if opcion == "1":
            elegido = self.cliente1
        elif opcion == "2":
            elegido = self.cliente2
        elif opcion == "3":
            elegido = self.cliente3
        else:
            print("No existe")
            return

        print("1. Depositar")
        print("2. Extraer")
        accion = input("Que desea hacer?: ")
        monto = int(input("Ingrese el monto: "))

        if accion == "1":
            elegido.depositar(monto)
        elif accion == "2":
            elegido.extraer(monto)
        else:
            print("Accion no valida")

    def deposito_total(self):
        total = self.cliente1.cantidad + self.cliente2.cantidad + self.cliente3.cantidad
        print("")
        print("- ESTADO FINAL DEL DIA -")
        self.cliente1.mostrar_total()
        self.cliente2.mostrar_total()
        self.cliente3.mostrar_total()
        print("Total depositado en el banco:", total)

mi_banco = Banco()
seguir = "si"

while seguir == "si":
    mi_banco.operar()
    seguir = input("\n¿Desea realizar otra operacion? (si/no): ")

mi_banco.deposito_total()