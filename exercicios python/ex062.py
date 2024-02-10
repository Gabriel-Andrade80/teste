'''t = p = int(input('primeiro termo: '))
r = int(input('razao: '))
print(p,end='')
c = 0
while c < 9:
    print('',end=' - ')
    t += r
    print(t,end='')
    c += 1
print('')
print('=-=' * 10)
while True:
    num = int(input('\nquantos termos a mais você deseja ver? '))
    if num == 0:
        print('STOP!')
        break
    else:
        c = 0
        t += r
        print(t,end='')
        while c < num-1:
            print('',end=' - ')
            t += r
            print(t,end='')
            c += 1'''
t = p = int(input('primeiro termo: '))
r = int(input('razao: '))
num = 10
while num != 0:
    c = 0
    while c < num:
        print(t,end=' - ')
        t += r
        c += 1
    print('PAUSA')
    num = int(input('quais termos a mais voce quer ver? '))
print('FIM')