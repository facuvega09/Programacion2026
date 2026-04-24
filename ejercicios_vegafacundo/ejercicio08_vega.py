import random

class Personaje:
    def __init__(self, nombre, vida, fuerza):
        self.nombre = nombre
        self.vida = vida
        self.fuerza = fuerza

    def atacar(self, oponente):
        danio = random.randint(self.fuerza - 5, self.fuerza + 5)
        oponente.vida = oponente.vida - danio
        print(self.nombre, "ataco a", oponente.nombre, "y le saco", danio, "de vida")
        if oponente.vida < 0:
            oponente.vida = 0

print("--- DUELO EN LA ARENA ---")
nombre_p = input("Nombre de tu personaje: ")

jugador = Personaje(nombre_p, 100, 20)
rival = Personaje("Enemigo", 100, 15)

while jugador.vida > 0 and rival.vida > 0:
    print("------------------------------")
    print("Estado actual:")
    print(jugador.nombre, ":", jugador.vida)
    print(rival.nombre, ":", rival.vida)
    
    print("\nTu turno: 1-Atacar / 2-Pasar")
    opcion = input("Elegir: ")
    
    if opcion == "1":
        jugador.atacar(rival)
    else:
        print(jugador.nombre, "no hizo nada este turno")
    
    if rival.vida > 0:
        print("\nTurno del sistema...")
        rival.atacar(jugador)

print("------------------------------")
if jugador.vida > 0:
    print("Ganaste la pelea!")
else:
    print("Perdiste... el enemigo te mato.")

print("GAME OVER")