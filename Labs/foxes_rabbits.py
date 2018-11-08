#Jeanna Shellenberger Section 061
import math


def bunnies(rabbits, foxes, years):
    y = 0
    R = [rabbits, 0]
    F = [foxes, 0]
    A, B, G, S = 0.04, 0.0005, 0.2, 0.00005
    while y < years:
        R[1] = R[0] + math.floor(R[0] * (A - B * F[0]))
        F[1] = F[0] - math.floor(F[0] * (G - S * R[0]))
        R[0] = R[1]
        F[0] = F[1]
        y += 1
    m = R[0]
    n = F[0]
    return m, n


if __name__ == "__main__":
    print("Welcome to Predator-Prey Model.")
    a = int(input("Enter Initial Rabbit Population:\n"))
    b = int(input("Enter Initial Fox Population:\n"))
    c = int(input("Enter Number of Years to Simulate:\n"))
    wild = bunnies(a, b, c)
    print('After', c, 'years there will be', wild[0], 'rabbits.')
    print('After', c, 'years there will be', wild[1], 'foxes.')
