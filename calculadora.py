class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = float(num1)
        self.num2 = float(num2)
    def sumar(self):
        suma = self.num1 + self.num2
        return suma
    def restar(self):
        resta = self.num1 - self.num2
        return resta
    def multiplicar(self):
        multi = self.num1 * self.num2
        return multi
    def dividir(self):
        divi = self.num1 / self.num2
        return divi
    
num1 = input("Ingrese un numero: ")
num2 = input("Ingrese otro numero: ")
    
sum = Calculadora(num1,num2)
sum.sumar()

    
    