class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre del alumno:", self.nombre)
        print("Nota:", self.nota)

    def resultado(self):
        if self.nota >= 7:
            print("Resultado:",self.nombre, "Aprobo")
        else:
            print("Resultado:", self.nombre, "Desaprobo")



alumno1 = Alumno("Facu", 8)
alumno1.imprimir()
alumno1.resultado()

alumno2 = Alumno("Julian", 4)
alumno2.imprimir()
alumno2.resultado()