x = input()
x = [int(i) for i in x.split()]
y = x.copy()
y.sort()
for i in y:
    print(i)

print()

for i in x:
    print(i)