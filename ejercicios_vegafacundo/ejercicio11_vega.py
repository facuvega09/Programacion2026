import random

class Hechicero:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 100
        self.mana = 50

    def lanzar_fuego(self, objetivo):
        if self.mana >= 10:
            self.mana = self.mana - 10
            danio = random.randint(20, 30)
            objetivo.vida = objetivo.vida - danio
            print(self.nombre, "lanza FUEGO a", objetivo.nombre, "y le saca", danio, "de vida")
        else:
            print(self.nombre, "no tiene mana suficiente para fuego!")

    def meditar(self):
        recupera = random.randint(15, 25)
        self.mana = self.mana + recupera
        print(self.nombre, "esta meditando y recupero", recupera, "de mana")

print("--- BATALLA DE HECHICEROS ---")
nom = input("Nombre de tu mago: ")

jugador = Hechicero(nom)
rival = Hechicero("Mago Oscuro")

combate_activo = 1

while combate_activo == 1:
    print("------------------------------")
    print(jugador.nombre, "| Vida:", jugador.vida, "| Mana:", jugador.mana)
    print(rival.nombre, "| Vida:", rival.vida, "| Mana:", rival.mana)
    
    print("\n¿Que hechizo usaras?")
    print("1- Bola de Fuego (Gasta 10 mana)")
    print("2- Meditar (Recupera mana)")
    opcion = input("Elegi: ")
    
    if opcion == "1":
        jugador.lanzar_fuego(rival)
    else:
        jugador.meditar()
    
    if rival.vida > 0:
        print("\nTurno del rival...")
        
        if rival.mana < 10:
            rival.meditar()
        else:
            rival.lanzar_fuego(jugador)
    
    if jugador.vida <= 0:
        combate_activo = 0
    if rival.vida <= 0:
        combate_activo = 0

print("------------------------------")
if jugador.vida > 0:
    print("¡Has ganado el duelo magico!")
else:
    print("Fuiste derrotado por el Mago Oscuro...")

print("GAME OVER")