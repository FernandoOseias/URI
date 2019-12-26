entrada = input()
a, b, c = [float(i) for i in entrada.split()]
c1 = (abs(a - b) < c and c < a + b)
c2 = (abs(a - c) < b and b < a + c)
c3 = (abs(b - c) < a and a < c + b)
if c1 and c2 and c3:
    perimetro = a + b + c
    print("Perimetro = {0:0.1f}".format(perimetro))
else:
    area = (a + b) * c /2
    print("Area = {0:0.1f}".format(area))
