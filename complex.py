#Jeanna Shellenberger Section 068
class ComplexNumber:
    def __init__(self, x, y): #making the numbers into floats
        self.__real = float(x)
        self.__img = float(y)

    def __str__(self):
        return str(self.__real) + ' ' + '+' + ' ' + str(self.__img) + 'i'

    def getReal(self): #pretty self explainitory
        return self.__real

    def getImaginary(self):
        return self.__img

#split the computations into 2 parts for simplification purposes
    def __add__(self, other):
        r = self.getReal()+other.getReal()
        i = self.getImaginary() + other.getImaginary()
        res = ComplexNumber(r,i)
        return res

    def __sub__(self, other):
        r = self.getReal() - other.getReal()
        i = self.getImaginary() - other.getImaginary()
        res = ComplexNumber(r, i)
        return res

    def __mul__(self, other):
        r = ((self.getReal() * other.getReal()) - (self.getImaginary() * other.getImaginary()))
        i = ((self.getReal() * other.getImaginary()) + (self.getImaginary() * other.getReal()))
        res = ComplexNumber(r, i)
        return res

    def __truediv__(self, other):
        r = ((self.getReal() * other.getReal()) + (self.getImaginary() * other.getImaginary())) / (other.getReal()** 2 + other.getImaginary()** 2)
        i = ((-self.getReal() * other.getImaginary()) + (self.getImaginary() * other.getReal())) / (other.getReal()** 2 + other.getImaginary()** 2)
        res = ComplexNumber(r, i)
        return res

#used if statements to keep computations simple
    def __pow__(self, exp):
        if exp < 0:
            self.__real = 1 / self.getReal()
            self.__img = 1 / self.getImaginary()
            return self.__pow__(exp * -1)
        elif exp == 0:
            return ComplexNumber(1, 0)
        elif exp > 0:
            return self * self.__pow__(exp - 1)

#test function
if __name__ == '__main__':
    c1 = ComplexNumber( 4, 3)
    c2 = ComplexNumber( 2, 8)
    print(c1)
    print(c1 + c2)
    print(c1 * c2)
    print(c1 / c2)
    print(c1 ** 3)
