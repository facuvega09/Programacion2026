import random

class Hechicero:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 100
        self.mana = 20



    def ataque_basico(self, objetivo):
        danio = random.randint(5, 10)
        objetivo.vida = objetivo.vida - danio
        if objetivo.vida < 0:
            objetivo.vida = 0
        print(self.nombre, "lanza chispas a", objetivo.nombre, "y quita", danio, "de vida.")



    def lanzar_hechizo(self, objetivo):
        if self.mana >= 20:
            self.mana = self.mana - 20
            danio = random.randint(20, 35)
            objetivo.vida = objetivo.vida - danio
            if objetivo.vida < 0:
                objetivo.vida = 0
            print(self.nombre, "Lanza una bola de fuego")
            print("Quita", danio, "de vida a", objetivo.nombre)
        else:
            print(self.nombre, "intento usar magia pero NO TIENE MANA.")
            print("Perdiste el turno por ambicioso.")



    def meditar(self):
        recuperado = random.randint(15, 25)
        self.mana = self.mana + recuperado
        print(self.nombre, "medita y recupera", recuperado, "de mana.")





print(" BATALLA DE HECHICEROS ")
nom = input("Nombre de tu mago: ")

jugador = Hechicero(nom)
rival = Hechicero("Mago Oscuro")

while jugador.vida > 0 and rival.vida > 0:
    print("\n------------------------------")
    print("ESTADO:")
    print(jugador.nombre, "| Vida:", jugador.vida, "| Mana:", jugador.mana)
    print(rival.nombre, "| Vida:", rival.vida, "| Mana:", rival.mana)
    
    print("\nTU TURNO:")
    print("1. Ataque basico (Gratis)")
    print("2. Bola de fuego (Cuesta 20 de Mana)")
    print("3. Meditar (Recuperar Mana)")
    opcion = input("Elegir accion: ")

    if opcion == "1":
        jugador.ataque_basico(rival)
    elif opcion == "2":
        jugador.lanzar_hechizo(rival)
    elif opcion == "3":
        jugador.meditar()
    else:
        print("Te confundiste de hechizo y no hiciste nada.")



    if rival.vida > 0:
        print("\nTurno del rival...")
        
        if rival.mana >= 20:
            rival.lanzar_hechizo(jugador)
        else:
            rival.ataque_basico(jugador)



print("\n------------------------------")
if jugador.vida > 0:
    print("¡Has ganado el duelo magico!")
else:
    print("Has sido derrotado")

print("GAME OVER")