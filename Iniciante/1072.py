n = int(input())
dentro = 0
fora = 0
for i in range(n):
    if 10 <= int(input()) <= 20:
        dentro += 1
    else:
        fora += 1

print('{0} in'.format(dentro))
print('{0} out'.format(fora))
