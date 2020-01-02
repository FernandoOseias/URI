x = int(input())

impares = [i for i in range(x, x+6*2+1) if ((i % 2) != 0) ]

for i in impares:
    print(i)