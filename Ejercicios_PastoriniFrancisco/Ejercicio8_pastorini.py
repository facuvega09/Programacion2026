import random

class Personaje:
    def __init__(self, nombre, vida, fuerza):
        self.nombre = nombre
        self.vida = vida
        self.fuerza = fuerza
        self.bloqueando = 0 


    def atacar(self, oponente):
        if oponente.bloqueando == 1:
            print(oponente.nombre, "SE CUBRIO! El ataque de", self.nombre, "no hizo daño.")
            oponente.bloqueando = 0
        else:
            danio = random.randint(self.fuerza - 5, self.fuerza + 5)
            oponente.vida = oponente.vida - danio
            if oponente.vida < 0:
                oponente.vida = 0
            print(self.nombre, "ataca a", oponente.nombre, "y le quita", danio, "de vida")


    def cubrirse(self):
        print(self.nombre, "se pone en guardia para el proximo ataque.")
        self.bloqueando = 1





print("DUELO EN LA ARENA")
nombre_p = input("Nombre de tu heroe: ")

jugador = Personaje(nombre_p, 100, 20)
rival = Personaje("Ogro", 100, 18)

while jugador.vida > 0 and rival.vida > 0:
    print("----------------------------------------")
    print("ESTADO:", jugador.nombre, ":", jugador.vida, "|", rival.nombre, ":", rival.vida)
    
    print("\nTU TURNO:")
    print("1. Pegar")
    print("2. Cubrirse (No recibes daño el proximo turno)")
    print("3. Pasar")
    opcion = input("Elegir accion: ")
    


    if opcion != "1":
        rival.bloqueando = 0

    if opcion == "1":
        jugador.atacar(rival)
    elif opcion == "2":
        jugador.cubrirse()
    else:
        print(jugador.nombre, "no hace nada...")

    if rival.vida > 0:
        print("\nTurno del enemigo...")
        rival.atacar(jugador)

print("----------------------------------------")
if jugador.vida > 0:
    print("VICTORIA: Has derrotado al enemigo.")
else:
    print("Has caido en combate...")

print("GAME OVER")