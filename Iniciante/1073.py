n = int(input())

pares = [i for i in range(2, n+1, 2)]
for i in pares:
    print('{0}^2 = {1}'.format(i, i**2))