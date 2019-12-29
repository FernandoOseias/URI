entrada = input()

entrada = [float(i) for i in entrada.split()]
entrada.sort(reverse=True)
a, b, c = entrada

if a >= (b + c):
    print("NAO FORMA TRIANGULO")
else:
    if a**2 == b**2 + c**2:
        print("TRIANGULO RETANGULO")
    if a**2 > b**2 + c**2:
        print("TRIANGULO OBTUSANGULO")
    if a**2 < b**2 + c**2:
        print("TRIANGULO ACUTANGULO")
    if a == b and b == c:
        print("TRIANGULO EQUILATERO")
    if (a == b) ^ (b == c):
        print("TRIANGULO ISOSCELES")
    
