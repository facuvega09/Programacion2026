import random

class Aventurero:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 100
        self.inventario = []
        self.fuerza_extra = 0




    def mostrar_estado(self):
        print("\n--- ESTADO DE", self.nombre, "---")
        print("Vida:", self.vida)
        print("Potenciador de Daño:", self.fuerza_extra)
        print("Mochila:", self.inventario)
        print("---------------------------")





    def usar_item(self, nombre_item):
        if nombre_item == "Pocion":
            self.vida = self.vida + 40
            if self.vida > 100: self.vida = 100
            print("Tomaste la pocion, Vida recuperada.")
        
        elif nombre_item == "Espada":
            self.fuerza_extra = self.fuerza_extra + 10
            print("Agarraste la espada, Tu proximo ataque sera mas fuerte.")
        

        if nombre_item in self.inventario:
            self.inventario.remove(nombre_item)







nom = input("Nombre del heroe: ")
jugador = Aventurero(nom)
jugando = "si"


while jugando == "si" and jugador.vida > 0:
    print("\nCaminas por la cueva...")
    evento = random.randint(1, 3)

    if evento == 1:
        objetos_posibles = ["Pocion", "Espada"]
        item = objetos_posibles[random.randint(0, 1)]
        print("¡ENCONTRASTE UN OBJETO:", item, "!")
        print("1. Guardar en mochila")
        print("2. Usar ahora")
        op = input("Eleccion: ")
        if op == "1":
            jugador.inventario.append(item)
        else:
            jugador.usar_item(item)

    elif evento == 2:
        print("Aparecio un moustro¡¡")
        danio_recibido = random.randint(20, 40)
        if "Espada" in jugador.inventario:
            print("Tenés una Espada en la mochila. ¿Querés usarla para defenderte? (si/no)")
            uso = input()
            if uso == "si":
                jugador.usar_item("Espada")
                danio_recibido = danio_recibido - 15
        
        jugador.vida = jugador.vida - danio_recibido
        print("El monstruo te hizo", danio_recibido, "de daño.")

    else:
        print("El camino está tranquilo por ahora...")

    jugador.mostrar_estado()

    if jugador.vida <= 0:
        print("\nHas muerto en la aventura...")
        break

    jugando = input("\n¿Seguir adelante? (si/no): ")

print("\nGAME OVER")