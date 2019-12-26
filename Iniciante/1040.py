entrada = input()
nota = entrada.split()
nota = [float(i) for i in nota]

media = (nota[0]*2 + nota[1] * 3 + nota[2] * 4 + nota[3] * 1)/10
print("Media: {0:0.1f}".format(media))
if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    nota_exame = float(input())
    print("Nota do exame: {0:0.1f}".format(nota_exame))
    media_final = (media + nota_exame)/2
    if media_final > 5:
        print("Aluno aprovado.")
    else:
        print("Aluno perovado.")
    print("Media final: {0:0.1f}".format(media_final))

