soma = 0
positivos = 0

for i in range(6):
    numero = float(input())
    if numero >= 0:
        positivos += 1
        soma += numero

media = soma / positivos

print('{0} valores positivos'.format(positivos))
print(round(media, 1))
