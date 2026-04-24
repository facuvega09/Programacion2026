import random
import time

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0

    def lanzar_dado(self):
        valor = random.randint(1, 6)
        self.puntos = self.puntos + valor
        print(self.nombre, "lanzó el dado y sacó un:", valor)

print("DESAFÍO DE DADOS")
nombre_u = input("Tu nombre: ")

usuario = Jugador(nombre_u)
rival1 = Jugador("Rival A")
rival2 = Jugador("Rival B")

rondas_totales = 3
ronda_actual = 1

while ronda_actual <= rondas_totales:
    print("------------------------------")
    print("RONDA NUMERO:", ronda_actual)
    
    print("Puntaje actual de", usuario.nombre, ":", usuario.puntos)
    input("Presiona ENTER para lanzar tu dado")
    usuario.lanzar_dado()
    
    print("\nTurno de los rivales")
    time.sleep(1)
    rival1.lanzar_dado()
    rival2.lanzar_dado()
    
    ronda_actual = ronda_actual + 1

print("------------------------------")
print("RESULTADOS FINALES:")
print(usuario.nombre, ":", usuario.puntos, "puntos")
print(rival1.nombre, ":", rival1.puntos, "puntos")
print(rival2.nombre, ":", rival2.puntos, "puntos")

if usuario.puntos >= rival1.puntos and usuario.puntos >= rival2.puntos:
    print("Felicidades! Ganaste el desafío")
elif rival1.puntos >= usuario.puntos and rival1.puntos >= rival2.puntos:
    print("Ganó el Rival A.")
else:
    print("Ganó el Rival B.")

print("GAME OVER")