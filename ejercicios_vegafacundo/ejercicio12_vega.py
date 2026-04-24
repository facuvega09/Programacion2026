import random

class Aventurero:
    def __init__(self, nombre):
        self.nombre = nombre
        self.inventario = [] 

    def guardar_objeto(self, objeto):
        self.inventario.append(objeto)
        print("Guardaste", objeto, "en tu mochila.")

    def usar_objeto(self, objeto):
        encontrado = 0
        for item in self.inventario:
            if item == objeto:
                encontrado = 1
        
        if encontrado == 1:
            print("Has usado el objeto:", objeto)
            self.inventario.remove(objeto)
        else:
            print("No tienes ese objeto en la mochila.")

    def mostrar_mochila(self):
        print("--- Tu Mochila ---")
        if len(self.inventario) == 0:
            print("Esta vacia.")
        else:
            for item in self.inventario:
                print("-", item)
        print("------------------")

print("--- AVENTURA Y OBJETOS ---")
nom = input("Nombre del aventurero: ")
jugador = Aventurero(nom)

objetos_posibles = ["Pocion", "Escudo", "Mapa", "Antorcha", "Cuerda"]
jugando = 1

while jugando == 1:
    objeto_encontrado = random.choice(objetos_posibles)
    print("\nCaminando por el bosque encontraste una:", objeto_encontrado)
    
    print("1- Guardar objeto")
    print("2- Descartar objeto")
    print("3- Ver mochila y usar algo")
    print("4- Salir de la aventura")
    
    opcion = input("Elegi una accion: ")
    
    if opcion == "1":
        jugador.guardar_objeto(objeto_encontrado)
    
    elif opcion == "2":
        print("Dejaste la", objeto_encontrado, "en el suelo.")
    
    elif opcion == "3":
        jugador.mostrar_mochila()
        if len(jugador.inventario) > 0:
            que_usar = input("Escribi el nombre del objeto para usarlo (o 'nada'): ")
            if que_usar != "nada":
                jugador.usar_objeto(que_usar)
    
    elif opcion == "4":
        print("Decidiste volver a casa.")
        jugando = 0

print("------------------------------")
print("Terminaste con estos objetos:")
jugador.mostrar_mochila()
print("GAME OVER")