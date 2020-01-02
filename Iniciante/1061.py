*x, dia_inicio = input().split()
dia_inicio = int(dia_inicio)
h_inicio, m_inicio, s_inicio = map(int, input().split(':'))

*x, dia_fim = input().split()
dia_fim = int(dia_fim)
h_fim, m_fim, s_fim = map(int, input().split(':'))


momento_inicio = dia_inicio + h_inicio/24 + (m_inicio/60)/24 + ((s_inicio/60)/60)/24
momento_fim = dia_fim + h_fim/24 + (m_fim/60)/24 + ((s_fim/60)/60)/24
duracao = momento_fim - momento_inicio

dia = round(duracao // 1)
horas = ((duracao%1)*24)
minutos = (horas%1)*60
horas = round(horas//1)
segundos = round((minutos%1) *60)
minutos = round(minutos // 1)

print('{0} dia(s)'.format(dia))
print('{0} hora(s)'.format(horas))
print('{0} minuto(s)'.format(minutos))
print('{0} segundo(s)'.format(segundos))