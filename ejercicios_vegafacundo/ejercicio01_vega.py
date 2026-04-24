class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir_datos(self):
        print("alumno: ",self.nota)
        print("nota: ",self.nota)

    def mostrar_resultado(self):
        if self.nota >= 6:
            print("resultado: ",self.nombre," aprobo")
        else:
            print("resultado: ",self.nombre," desaprobo")

alumno1 = Alumno("Sofía", 8.5)
alumno2 = Alumno("Carlos", 4.0)

print("Información Alumno 1")
alumno1.imprimir_datos()
alumno1.mostrar_resultado()

print("\nInformación Alumno 2")
alumno2.imprimir_datos()
alumno2.mostrar_resultado()