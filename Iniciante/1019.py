x = int(input())
h = x // (60*60)
m = x % (60*60)
s = m % 60
m = m // 60
print('{0}:{1}:{2}'.format(h,m,s))