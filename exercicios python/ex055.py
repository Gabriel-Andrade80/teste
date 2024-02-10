ma = 0
me = -1
for i in range(1,6):
    peso = float(input(f'peso da {i}º pessoa: '))
    if me == -1:
        me = peso
    if peso > ma:
        ma = peso
    if peso < me:
        me = peso
print('maior peso: {}kg'.format(ma))
print('menor peso: {}kg'.format(me))
