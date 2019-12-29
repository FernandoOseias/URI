
#entrada = input()

#a, b = entrada.split()
#a = int(a)
#b = int(b)


a,b=map(int, input().split())


#c1 = a % b
#c2 = b % a

#if (a%b == 0) or (b % a == 0): 
#    print("Sao Multiplos")
#else:
#    print("Não sao Multiplos")


if (a%b==0)or(b%a==0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")