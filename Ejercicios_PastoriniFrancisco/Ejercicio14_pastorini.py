import random

class Torre:
    def __init__(self, nombre):
        self.nombre = nombre
        self.resistencia = 100
        self.escudo_activo = 0




    def recibir_ataque(self, danio):
        if self.escudo_activo == 1:
            danio_reducido = int(danio * 0.25)
            self.resistencia = self.resistencia - danio_reducido
            print("¡El escudo absorbió el 75% del impacto!")
            print("La torre solo recibió", danio_reducido, "de daño.")
            self.escudo_activo = 0 
        else:
            self.resistencia = self.resistencia - danio
            print("¡Impacto directo! La torre perdió", danio, "de resistencia.")
        
        # Evitamos que la vida sea negativa
        if self.resistencia < 0:
            self.resistencia = 0




    def reparar(self):
        curacion = random.randint(15, 25)
        self.resistencia = self.resistencia + curacion
        if self.resistencia > 100:
            self.resistencia = 100
        print("Los ingenieros repararon la torre. +", curacion, "de resistencia.")




    def activar_escudo(self):
        print("¡Sistemas de defensa activados! El escudo cubrirá parte del próximo ataque.")
        self.escudo_activo = 1





print("--- ÚLTIMA DEFENSA ---")
nom_torre = input("Dale un nombre a tu fortaleza: ")
torre = Torre(nom_torre)

oleada = 1

while torre.resistencia > 0:
    print("\n================================")
    print("ESTADO DE LA TORRE:", torre.nombre)
    print("RESISTENCIA:", torre.resistencia, "/ 100")
    print("OLEADA NÚMERO:", oleada)
    print("--------------------------------")
    
    # Menú de acciones
    print("¿Qué orden das a la defensa?")
    print("1. Reparar torre")
    print("2. Activar escudo (Reduce 75% el daño)")
    print("3. Contraatacar (Baja el ataque enemigo)")
    
    accion = input("Elegir acción: ")

    print("\n--- ¡VIENEN LOS ENEMIGOS! ---")
    ataque_enemigo = random.randint(25, 50)
    
    if accion == "1":
        torre.reparar()
    elif accion == "2":
        torre.activar_escudo()
    elif accion == "3":
        reduccion = random.randint(15, 20)
        ataque_enemigo = ataque_enemigo - reduccion
        print("¡El contraataque debilitó al enemigo!")
    else:
        print("Dudaste... los enemigos atacan con todo.")

    torre.recibir_ataque(ataque_enemigo)
    
    oleada = oleada + 1
    if torre.resistencia > 0:
        input("\nPresiona ENTER para la siguiente oleada...")

print("\n================================")
print("LA TORRE HA CAÍDO.")
print("Resististe un total de", oleada - 1, "oleadas.")
print("GAME OVER")