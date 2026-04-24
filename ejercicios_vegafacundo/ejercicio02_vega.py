class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print("nombre: ", self.nombre)
        print("edad: ",self.edad,"años")

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            print(self.nombre,"es mayor de edad")
        else:
            print(self.nombre,"es menor de edad")


persona1 = Persona("Lucía", 25)

persona2 = Persona("Julián", 16)

print("Datos Persona 1")
persona1.mostrar_datos()
persona1.es_mayor_de_edad()

print("Datos Persona 2")
persona2.mostrar_datos()
persona2.es_mayor_de_edad()