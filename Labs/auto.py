#Jeanna Shellenberger Section 061
import math


def hypotenuse(a, b):
    c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
    return c


if __name__ == "__main__":
    print("Hypotenus Example")
    a = int(input("Enter Side One:\n"))
    b = int(input("Enter Side Two:\n"))

    print("Hypotenuse is %0.4f" % (hypotenuse(a, b)))
