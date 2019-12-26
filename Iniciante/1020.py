idadeDias = int(input())

anos = idadeDias // 365
meses = idadeDias % 365
dias = meses % 30
meses = meses // 30
print('{0} ano(s)'.format(anos))
print('{0} mes(es)'.format(meses))
print('{0} dia(s)'.format(dias))