pares = 0
impares = 0
positivos = 0
negativos = 0

n = int(input())
entradas = []

for i in range(n):
    entradas.append(int(input()))

for numero in entradas:
    mensagem = ''
    if (numero % 2) == 0:
        mensagem += 'EVEN'
    else:
        mensagem += 'ODD'
    
    if numero > 0:
        mensagem += ' POSITIVE'
    elif numero < 0:
        mensagem += ' NEGATIVE'
    else:
        mensagem = 'NULL'

    print(mensagem)

    