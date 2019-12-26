import math

entrada = input()
A, B = entrada.split()
A = float(A)
B = float(B)

entrada = input()
C, D = entrada.split()
C = float(C)
D = float(D)

soma = pow(C-A,2) + pow(D-B,2)
distancia = math.sqrt(soma)

print("{0:.4f}".format(distancia))