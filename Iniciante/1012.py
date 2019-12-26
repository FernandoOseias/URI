entrada = input()
A, B, C = entrada.split()
A = float(A)
B = float(B)
C = float(C)

pi = 3.14159

areaTriangulo = (A * C) / 2
areaCirculo = pi * C *C
areaTrapezio = ((A + B) / 2) * C
areaRetangulo = A * B
areaQuadrado = B * B


print("TRIANGULO: {0:.3f}".format(areaTriangulo))
print("CIRCULO: {0:.3f}".format(areaCirculo))
print("TRAPEZIO: {0:.3f}".format(areaTrapezio))
print("QUADRADO: {0:.3f}".format(areaQuadrado))
print("RETANGULO: {0:.3f}".format(areaRetangulo))

