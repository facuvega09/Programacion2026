import random

class Auto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.distancia_recorrida = 0

    def acelerar(self):
        suerte = random.randint(1, 10)
        
        if suerte <= 4:
            print(self.nombre, "intentó acelerar mucho pero el motor falló! Avanzó 0 metros.")
        else:
            avance = random.randint(15, 25)
            self.distancia_recorrida = self.distancia_recorrida + avance
            print(self.nombre, "¡Piso a fondo¡ Avanzó", avance, "metros.")

    def mantener(self):
        avance = random.randint(7, 12)
        self.distancia_recorrida = self.distancia_recorrida + avance
        print(self.nombre, "va a ritmo tranquilo y avanzó", avance, "metros.")



print("--- GRAN CARRERA ---")
nombre_u = input("Nombre de tu auto: ")

jugador = Auto(nombre_u)
rival = Auto("Rayo Veloz")

meta = 100

while jugador.distancia_recorrida < meta and rival.distancia_recorrida < meta:
    print("\n------------------------------")
    print("DISTANCIAS: Tu:", jugador.distancia_recorrida, "| Rival:", rival.distancia_recorrida)
    
    print("1. Acelerar a fondo (Podés avanzar MUCHO o FALLAR)")
    print("2. Mantener (Avance seguro pero corto)")
    opcion = input("Elegí tu acción: ")

    if opcion == "1":
        jugador.acelerar()
    else:
        jugador.mantener()


    if rival.distancia_recorrida < meta:
        print("\nTurno del rival...")
        rival.mantener()


print("\n--- RESULTADO FINAL ---")
if jugador.distancia_recorrida >= meta:
    print("¡GANASTE! Cruzaste la meta.")
else:
    print("Perdiste... el rival llegó antes.")

print("GAME OVER")