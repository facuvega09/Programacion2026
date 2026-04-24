import random

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0
        self.jugando = 1 # 1: sigue, 0: se plantó o perdió

  
  
    def lanzar_dado(self):
        tiro = random.randint(1, 6)
        self.puntos = self.puntos + tiro
        print(self.nombre, "sacó un:", tiro, "| Total:", self.puntos)
        
        if self.puntos > 15:
            print("¡", self.nombre, "se pasó de 15!")
            self.jugando = 0

  
  
  
    def plantarse(self):
        print(self.nombre, "se ha plantado.")
        self.jugando = 0





print("CARRERA AL 15:")
nom = input("Tu nombre: ")
usuario = Jugador(nom)
bot = Jugador("Bot-Rival")



while usuario.jugando == 1 or bot.jugando == 1:
    print("\n================================")
    print("MARCADOR: ", usuario.nombre, ":", usuario.puntos, " | ", bot.nombre, ":", bot.puntos)
    

    if usuario.jugando == 1:
        print("\n--- TU TURNO ---")
        print("1. Lanzar dado")
        print("2. Plantarse")
        opcion = input("Elegí: ")
        if opcion == "1":
            usuario.lanzar_dado()
        else:
            usuario.plantarse()
    else:
        print("\n", usuario.nombre, "está plantado o fuera.")


    if bot.jugando == 1:
        print("\n--- TURNO DEL RIVAL ---")
        # El bot ahora es más inteligente: si vos tenés más que él, se arriesga
        if bot.puntos < 11 or (bot.puntos < usuario.puntos and usuario.puntos <= 15):
            bot.lanzar_dado()
        else:
            bot.plantarse()
    else:
        print("\nEl Rival está plantado o fuera.")





print("\n================================")
print("PUNTAJES FINALES:")
print(usuario.nombre, ":", usuario.puntos)
print(bot.nombre, ":", bot.puntos)

# Lógica de victoria corregida para turnos simultáneos
if usuario.puntos > 15 and bot.puntos > 15:
    print("¡AMBOS SE PASARON! Nadie gana.")
elif usuario.puntos > 15:
    print("Perdiste... te pasaste de 15.")
elif bot.puntos > 15:
    print("¡GANASTE! El bot se pasó.")
elif usuario.puntos > bot.puntos:
    print("¡GANASTE! Estuviste más cerca.")
elif bot.puntos > usuario.puntos:
    print("Perdiste... el bot estuvo más cerca.")
else:
    print("¡EMPATE!")

print("\nGAME OVER")