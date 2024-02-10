v = []
for i in range(5):
    num = int(input('numero: '))
    v.append(num)
print(f'valores digitados: {v}')
print(f'maior valor: {max(v)} na posição',end=' ')
for ind,num in enumerate(v):
    if num == max(v):
        print(f'{ind}...',end=' ')
print()
print(f'menor valor: {min(v)} na posição',end=' ')
for ind,num in enumerate(v):
    if num == min(v):
        print(f'{ind}...',end=' ')
