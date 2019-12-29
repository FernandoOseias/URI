salario = float(input())

if salario <= 400:
    percentual = 0.15
elif salario <= 800:
    percentual = 0.12
elif salario <= 1200:
    percentual = 0.10
elif salario <= 2000:
    percentual = 0.07
else:
    percentual = 0.04

reajuste = round(salario*percentual,2)
novo_salario = round(salario + reajuste,2)
print('Novo salario: {0:0.2f}'.format(novo_salario))
print('Reajuste ganho: {0:0.2f}'.format(reajuste))
print('Em percentual: {0} %'.format(int(percentual*100)))