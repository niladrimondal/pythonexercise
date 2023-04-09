class Calculator:
    def __init__(self,num1,num2):
        self.a = num1
        self.b = num2
        
    def sum(self):
        return self.a + self.b

    def substruct(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b

print('Enter the First Numer')
num1 = int(input())
print('Enter the Second Numer')
num2 = int(input())

calc = Calculator(num1,num2)
print('Sum of the Two Numers')
print(calc.sum())
print('Substruction of the Two Numers')
print(calc.substruct())
print('Multiplication of the Two Numers')
print(calc.multiply())
print('Division of the Two Numers')
print(calc.divide())