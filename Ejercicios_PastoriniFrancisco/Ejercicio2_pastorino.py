class persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    
    def datos(self):
        print("nombre",self.nombre)
        print("edad", self.edad)
    
    def verificar(self):
        if self.edad >= 18:
            print("es mayor de edad")
        else:
            print("es menor de edad")
            
p1=persona("pablo",15)
p1.datos()
p1.verificar()

p2=persona("juan", 22)
p2.datos()
p2.verificar()
