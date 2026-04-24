class calculadora: 
    def __init__(self):
        self.numero1=int(input("ingrese primer numero:"))
        self.numero2=int(input("ingrese segundo numero: "))
        
    def sumar(self):
        self.resultado=self.numero1 + self.numero2
        print("la suma es",self.resultado)
        
        
    def resta(self):
        self.resultado=self.numero1 - self.numero2
        print("la resta es",self.resultado)
        
    def multiplicacion(self):
        self.resultado=self.numero1*self.numero2
        print("la multiplicacion es",self.resultado)
        
    def divicion(self):
        if self.numero2 != 0:
            self.resultado=self.numero1/self.numero2
            print("la divicion es",self.resultado)
            
        else:
            print("no se puede dividir por 0")
            
c1=calculadora()
c1.sumar()
c1.resta()
c1.multiplicacion ()
c1.divicion()