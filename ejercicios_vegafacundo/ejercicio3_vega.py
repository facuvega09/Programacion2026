class triangulin:
    def __init__(self,a,b,c):
        self.lado1=a
        self.lado2=b
        self.lado3=c
        
    def mayoraso(self):
        if self.lado1>self.lado2:
            may=self.lado1
        else:
            may=self.lado2
            
        if may>self.lado3:
            may
            
        else:
            may=self.lado3
            
        print("el mayor es", may)
        
    def clasification(self):
        if self.lado1==self.lado2==self.lado3:
            print("triangulo equilatero")
            
        elif self.lado1==self.lado2 or self.lado1==self.lado3 or self.lado2==self.lado3:
            print("triangulo isoceles")
            
        else:
            print("triangulo escaleno")
            
triangle1=triangulin(7,7,8)
triangle1.mayoraso()
triangle1.clasification()        