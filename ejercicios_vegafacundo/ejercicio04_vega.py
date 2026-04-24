class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sumar(self):
        resultado = self.num1 + self.num2
        print("La suma es:", resultado)

    def restar(self):
        resultado = self.num1 - self.num2
        print("La resta es:", resultado)

    def multiplicar(self):
        resultado = self.num1 * self.num2
        print("La multiplicación es:", resultado)

    def dividir(self):
        if self.num2 != 0:
            resultado = self.num1 / self.num2
            print("La división es:", resultado)
        else:
            print("Error: No se puede dividir por cero.")

v1 = int(input("Ingrese el primer número: "))
v2 = int(input("Ingrese el segundo número: "))

mi_calculadora = Calculadora(v1, v2)

mi_calculadora.sumar()
mi_calculadora.restar()
mi_calculadora.multiplicar()
mi_calculadora.dividir()