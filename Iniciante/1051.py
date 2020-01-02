salario = float(input())

if 0 <= salario <= 2000:
    print('Isento')
    exit()
elif 2000 < salario <= 3000:
    imposto = (salario - 2000) * 0.08
elif 3000 < salario <= 4500:
    imposto = (salario - 3000) * 0.18 + ((3000 - 2000) * 0.08)
elif salario >= 4500:
    imposto = (salario - 4500) * 0.28 + ((4500- 3000) * 0.18) + ((3000-2000)*0.08)
    
print('R$ {0:0.02f}'.format(imposto))