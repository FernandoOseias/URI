pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(5):
    numero = int(input())
    if (numero % 2) == 0:
        pares += 1
    else:
        impares += 1
    
    if numero > 0:
        positivos +=1
    elif numero < 0:
        negativos += 1

print('{0} valor(es) par(es)'.format(pares))
print('{0} valor(es) impar(es)'.format(impares))
print('{0} valor(es) positivo(s)'.format(positivos))
print('{0} valor(es) negativo(s)'.format(negativos))


