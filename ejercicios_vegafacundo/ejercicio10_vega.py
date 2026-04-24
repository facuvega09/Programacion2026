import random
import time

class Auto:
    def __init__(self, marca):
        self.marca = marca
        self.distancia = 0

    def acelerar(self):
        avance = random.randint(10, 20)
        self.distancia = self.distancia + avance
        print(self.marca, "ha avanzado", avance, "metros.")

    def frenar(self):
        # El freno hace que avance poco o nada
        avance = random.randint(0, 5)
        self.distancia = self.distancia + avance
        print(self.marca, "frenó un poco y solo avanzó", avance, "metros.")

# --- INICIO DEL JUEGO ---
print("--- LA GRAN CARRERA ---")
nombre_auto = input("¿Que marca es tu auto?: ")

jugador = Auto(nombre_auto)
rival = Auto("Rival Pro")

meta = 100
en_carrera = True

while en_carrera == True:
    print("------------------------------")
    print("DISTANCIAS:")
    print(jugador.marca, ":", jugador.distancia, "m")
    print(rival.marca, ":", rival.distancia, "m")
    
    # Turno del usuario
    print("\nAcciones: 1-Acelerar a fondo / 2-Maniobrar (lento)")
    opcion = input("Tu accion: ")
    
    if opcion == "1":
        jugador.acelerar()
    else:
        jugador.frenar()
    
    # Turno del rival automático
    print("Turno del rival...")
    time.sleep(1)
    rival.acelerar()
    
    # Chequear si alguien llego a la meta
    if jugador.distancia >= meta or rival.distancia >= meta:
        en_carrera = False

# Final de la carrera
print("------------------------------")
print("RESULTADOS FINALES:")
print(jugador.marca, ":", jugador.distancia, "m")
print(rival.marca, ":", rival.distancia, "m")

if jugador.distancia >= rival.distancia:
    print("¡Felicidades! Ganaste la carrera.")
else:
    print("El rival cruzó la meta primero. Perdiste.")

print("GAME OVER")