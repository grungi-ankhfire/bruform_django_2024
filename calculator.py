class Calculator:

    def __init__(self):
        self.result = 0

    def add(self, amount):
        self.result += amount

    def __str__(self):
        return f"Calculator with result {self.result} !"


calc = Calculator()
calc2 = Calculator()
calc.add(20)
print(calc.result)
print(calc)
print(calc2)