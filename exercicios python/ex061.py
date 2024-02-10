t = p = int(input('primeiro termo: '))
r = int(input('razao: '))
print(p,end='')
c = 0
while c < 9:
    print('',end=' - ')
    t += r
    print(t,end='')
    c += 1