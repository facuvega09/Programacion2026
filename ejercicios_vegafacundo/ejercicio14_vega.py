import random
import time

class Torre:
    def __init__(self, nombre):
        self.nombre = nombre
        self.resistencia = 100
        self.escudo_activo = 0 

    def recibir_ataque(self):
        danio = random.randint(15, 25)
        if self.escudo_activo == 1:
            danio = danio // 2
            print("El escudo absorbio parte del impacto")
        
        self.resistencia = self.resistencia - danio
        print("La torre recibio", danio, "puntos de danio")
        
        if self.resistencia < 0:
            self.resistencia = 0

    def reparar(self):
        arreglo = random.randint(5, 10)
        self.resistencia = self.resistencia + arreglo
        print("Trabajadores reparando Se recuperaron", arreglo, "puntos.")


print("ULTIMA DEFENSA")
nom_torre = input("Dale un nombre a tu torre: ")
mi_torre = Torre(nom_torre)

torre_en_pie = 1

while torre_en_pie == 1:
    print("------------------------------")
    print("ESTADO DE LA TORRE:", mi_torre.nombre)
    print("Resistencia actual:", mi_torre.resistencia)
    
    print("\nSe acerca una horda de enemigos")
    print("1- Activar Escudo (reduce proximo danio)")
    print("2- Reparar estructura")
    print("3- No hacer nada")
    
    opcion = input("Elegi tu defensa: ")
    
    if opcion == "1":
        mi_torre.escudo_activo = 1
        print("Escudos levantados.")
    elif opcion == "2":
        mi_torre.escudo_activo = 0
        mi_torre.reparar()
    else:
        mi_torre.escudo_activo = 0
        print("La torre espera el impacto sin proteccion.")

    time.sleep(1)
    mi_torre.recibir_ataque()
    
    mi_torre.escudo_activo = 0
    
    if mi_torre.resistencia <= 0:
        torre_en_pie = 0

print("------------------------------")
print("La torre", mi_torre.nombre, "ha caído. El territorio fue invadido.")
print("GAME OVER")