inicio, fim = map(int, input().split())


if(inicio < fim):
    duracao = fim - inicio
    print('O JOGO DUROU {0} HORA(S)'.format(duracao))
elif (inicio > fim):
    duracao = 24 - inicio + fim
    print('O JOGO DUROU {0} HORA(S)'.format(duracao))
else:
    print('O JOGO DUROU 24 HORA(S)')