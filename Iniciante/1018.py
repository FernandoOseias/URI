notas = [100, 50, 20, 10, 5, 2, 1]

qtdes = []
valor = int(input())
print(valor)
for nota in notas:
    qtde = valor // nota
    qtdes.append(qtde)
    valor = valor % nota
    print("{0:d} nota(s) de R$ {1:0.2f}".format(qtde, nota).replace('.',','))

