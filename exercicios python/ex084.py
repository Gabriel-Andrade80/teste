exame = []
info = []
leves = []
pesados = []
p = 0
while True:
    info.append(input('nome: '))
    info.append(float(input('peso: ')))
    exame.append(info[:])
    info.clear()
    p += 1
    resp = input('Quer continuar [S/N]? ').lower().strip()[0]
    if resp == 'n':
        break
ma = me = exame[0][1]
print(f'{p} pessoas cadastradas.')
for peso in exame:
    if peso[1] > ma:
        ma = peso[1]
    if peso[1] < me:
        me = peso[1]
for g in exame:
    if g[1] == ma:
        pesados.append(g[0])
    if g[1] == me:
        leves.append(g[0])
print(f'maior peso: {ma}; ',end='')
print(f'peso de',end=' ')
for i in pesados:
    print(f'[{i}]',end=' ')
print(f'\nmenor peso: {me}; ',end='')
print(f'peso de',end=' ')
for i in leves:
    print(f'[{i}]',end=' ')