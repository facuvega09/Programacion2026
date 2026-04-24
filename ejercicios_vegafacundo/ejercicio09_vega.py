import random

class Cofre:
    def __init__(self):
        self.esta_abierto = False
        self.monedas = random.randint(10, 50)

    def abrir(self):
        if self.esta_abierto == False:
            self.esta_abierto = True
            print("Has abierto el cofre.")
        else:
            print("El cofre ya estaba abierto.")


print("--- BUSQUEDA DEL TESORO ---")
inventario_monedas = 0
continuar = "si"

while continuar == "si":
    print("------------------------------")
    print("Explorando la cueva...")
    
    cofre_actual = Cofre()
    print("¡Encontraste un cofre!")
    
    accion = ""
    while accion != "3":
        print("\nMonedas actuales:", inventario_monedas)
        if cofre_actual.esta_abierto:
            estado = "Abierto"
        else:
            estado = "Cerrado"
        print("Estado del cofre:", estado)
        
        print("1- Abrir cofre")
        print("2- Recolectar monedas")
        print("3- Seguir caminando")
        accion = input("¿Que quieres hacer?: ")
        
        if accion == "1":
            cofre_actual.abrir()
        
        elif accion == "2":
            if cofre_actual.esta_abierto == True:
                if cofre_actual.monedas > 0:
                    print("Recogiste", cofre_actual.monedas, "monedas!")
                    inventario_monedas = inventario_monedas + cofre_actual.monedas
                    cofre_actual.monedas = 0 
                else:
                    print("El cofre esta vacio.")
            else:
                print("No puedes sacar monedas de un cofre cerrado.")
        
        elif accion == "3":
            print("Dejas el cofre atras...")
    
    continuar = input("\n¿Quieres seguir explorando la cueva? (si/no): ")

print("------------------------------")
print("Terminaste la exploracion con", inventario_monedas, "monedas en total.")
print("GAME OVER")