class arithmetic_operator:
    def __init__(self, a,b):
        self.a = a
        self.b = b
    def addition(self):
        return self.a + self.b
    def subtraction(self):
        return self.a - self.b
    def division(self):
        return self.a / self.b
    def multiplication(self):
        return self.a * self.b

if __name__ == '__main__':
    x= arithmetic_operator(10,20)
    print(x.addition())
    print(x.subtraction())
    print(x.multiplication())
    print(x.division())
    y= arithmetic_operator(30,20)
    print(y.addition())
    