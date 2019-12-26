entrada = input()
A, B = entrada.split()
cod = int(A)
qtde = int(B)

precos = [4, 4.5, 5, 2, 1.5]

precoTotal = qtde * precos[cod-1]

print("Total: R$ {0:.2f}".format(precoTotal))