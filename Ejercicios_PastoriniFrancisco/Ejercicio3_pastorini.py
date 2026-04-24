class triangulo:
    def __init__(self,a,b,c):
        self.lado1=a
        self.lado2=b
        self.lado3=c
        
    def mayor(self):
        if self.lado1>self.lado2:
            may=self.lado1
        else:
            may=self.lado2
            
        if may>self.lado3:
            may
        
        else:
            may=self.lado3
        
        print("el mayor es", may)

    def clasificacion(self):
        if self.lado1==self.lado2==self.lado3:
            print("triangulo equilatero")
            
        elif self.lado1==self.lado2 or self.lado1==self.lado3 or self.lado2==self.lado3:
            print("triangulo isoceles")
            
        else:
            print("tirnagulo escaleno")
            
t1=triangulo(7,7,7)
t1.mayor()
t1.clasificacion()

t2=triangulo(7,7,10)
t2.mayor()
t2.clasificacion()

t3=triangulo(5,7,10)
t3.mayor()
t3.clasificacion()