entrada = input()
A, B, C = entrada.split()
A = float(A)
B = float(B)
C = float(C)

def maiorAB (a, b):
    return int((a+b+abs(a-b))/2)

print("{0:d} eh o maior".format(maiorAB(A,maiorAB(B,C))))