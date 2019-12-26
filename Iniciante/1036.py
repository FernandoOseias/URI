from math import sqrt

entrada = input()
A, B, C = entrada.split()
a = float(A)
b = float(B)
c = float(C)

delta = b * b - (4*a*c)

if delta < 0 or a == 0:
    print("Impossivel calcular")
else:
    r1 = (-b + sqrt(delta))/(2*a)
    r2 = (-b - sqrt(delta))/(2*a)
    print("R1 = {0:.5f}".format(r1))
    print("R2 = {0:.5f}".format(r2))

