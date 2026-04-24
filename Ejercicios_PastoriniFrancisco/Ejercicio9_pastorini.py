import random

class Cofre:
    def __init__(self):
        self.estado = random.randint(0, 1) 
        self.monedas = random.randint(10, 50)

    def mostrar_estado(self):
        if self.estado == 1:
            print("Estado del cofre: CERRADO")
        else:
            print("Estado del cofre: ABIERTO")
        print("Monedas en su interior:", self.monedas)

    def abrir(self):
        if self.estado == 1:
            print("¡Has abierto el cofre!")
            self.estado = 0
        else:
            print("El cofre ya estaba abierto.")

class Explorador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.bolsa_monedas = 0

    def recolectar(self, cofre):
        if cofre.estado == 0:
            print("Has recogido", cofre.monedas, "monedas.")
            self.bolsa_monedas = self.bolsa_monedas + cofre.monedas
            cofre.monedas = 0 
        else:
            print("No puedes recoger monedas de un cofre cerrado. Intenta abrirlo primero.")





print("EL TESORO ESCONDIDO")
nombre_u = input("Nombre del explorador: ")
jugador = Explorador(nombre_u)

continuar = "si"

while continuar == "si":
    print("\n------------------------------")
    print("Explorando la cueva...")
    cofre_actual = Cofre()
    
    print("¡Has encontrado un cofre!")
    cofre_actual.mostrar_estado()
    
    
    menu_cofre = "si"
    while menu_cofre == "si":
        print("\n¿Que quieres hacer con este cofre?")
        print("1. Intentar abrirlo")
        print("2. Recolectar monedas")
        print("3. Dejar el cofre y seguir explorando")
        accion = input("Elegir opcion: ")
        
        if accion == "1":
            cofre_actual.abrir()
        elif accion == "2":
            jugador.recolectar(cofre_actual)
        elif accion == "3":
            menu_cofre = "no"
        else:
            print("Opcion no valida")
            
    print("\nMonedas totales en tu bolsa:", jugador.bolsa_monedas)
    continuar = input("¿Deseas seguir explorando la cueva? (si/no): ")

print("\n--- RESUMEN FINAL ---")
print("Explorador:", jugador.nombre)
print("Total de monedas conseguidas:", jugador.bolsa_monedas)
print("GAME OVER")