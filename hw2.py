#Jeanna Shellenberger Section 068
from complex import ComplexNumber #accessing class
import sys

#creating function one
def a(c, k):
    x = ComplexNumber(1, 0)
    for i in range(k):
         a = c ** (i + 1)
         x += a
    return x

#creating function two
def b(c, k):
    y = ComplexNumber(1, 0)
    b = (y - (c ** (k + 1))) / (y - c)
    return b

#oh jeez rick
r = float(sys.argv[1]) #command line arguments
i = float(sys.argv[2])
c = ComplexNumber(r, i)
k = int(sys.argv[3])

func1 = a(c, k)
func2 = b(c, k)

#print statements
print('For complex number', c, 'and k =', k)
print('a(' + str(c) + ', ' + str(k) + ') = ' + str(func1))
print('b(' + str(c) + ', ' + str(k) + ') = ' + str(func1))