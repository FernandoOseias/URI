ini_h, ini_m, fim_h, fim_min = map(int, input().split())

inicio = ini_h + ini_m / 60
fim = fim_h + fim_min / 60

if(inicio < fim):
    duracao = fim - inicio
    duracao_h = round(duracao // 1)
    duracao_min = round((duracao % 1) * 60)
    print('O JOGO DUROU {0} HORA(S) E {1} MINUTO(S)'.format(duracao_h, duracao_min))
elif (inicio > fim):
    duracao = 24 - inicio + fim
    duracao_h = round(duracao // 1)
    duracao_min = round((duracao % 1) * 60)
    print('O JOGO DUROU {0} HORA(S) E {1} MINUTO(S)'.format(duracao_h, duracao_min))
else:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')