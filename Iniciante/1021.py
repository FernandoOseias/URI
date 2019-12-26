notas = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]

qtdes = []
valor = float(input()) + 0.001
print("NOTAS:")
for nota in notas:
    qtde = int(valor // nota)
    qtdes.append(qtde)
    valor = valor % nota
    if (nota >1):
        #print("{0} nota(s) de R$ {1:0.2f}".format(qtde, nota).replace('.',','))
        print("{0} nota(s) de R$ {1:0.2f}".format(qtde, nota))
    elif (nota == 1):
        print('MOEDAS:')
        #print("{0} moeda(s) de R$ {1:0.2f}".format(qtde, nota).replace('.',','))
        print("{0} moeda(s) de R$ {1:0.2f}".format(qtde, nota))
    else:
        #print("{0} moeda(s) de R$ {1:0.2f}".format(qtde, nota).replace('.',','))
        print("{0} moeda(s) de R$ {1:0.2f}".format(qtde, nota))

