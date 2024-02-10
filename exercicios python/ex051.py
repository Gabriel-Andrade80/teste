t = p = int(input('primeiro termo: '))
r = int(input('razao: '))
print(p,end='')
for i in range(9):
    print('',end=' - ')
    t += r
    print(t,end='')
