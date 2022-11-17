
class Complex(object):
    def __init__(self, real, imaginary):
        self.real=real
        self.imaginary=imaginary
    def __add__(self, no):
        self.real= self.real+no.real
        self.imaginary=self.imaginary+no.imaginary
        return complex(self.real, self.imaginary)
    def __sub__(self, no):
        self.real= self.real-no.real
        self.imaginary=self.imaginary-no.imaginary
        return complex(self.real, self.imaginary)
    def __mul__(self, no):
        self.real= self.real*no.real
        self.imaginary=self.imaginary*no.imaginary
        return complex(self.real, self.imaginary)
    def __truediv__(self, no):
        self.real= self.real/no.real
        self.imaginary=self.imaginary/no.imaginary
        return complex(self.real, self.imaginary)
    def mod(self):
        self.real= self.real
        self.imaginary=self.imaginary
        return complex(self.real, self.imaginary)
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result
#x= 2+1i
#y= 5+6i
if __name__ == '__main__':
    # c = map(2 1)
    # d = map(5 6)
    x = Complex(2,1)
    y = Complex(5,6)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')