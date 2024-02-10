v = []
for i in range(5):
    num = int(input('numero: '))
    if (i == 0) or (num > v[-1]):
        v.append(num)
        print(f'adicionando ao final da lista...')
    else:
        pos = 0
        while pos < len(v):
            if num <= v[pos]:
                v.insert(pos,num)
                print(f'Adicionando na posição {pos}...')
                break
            pos += 1
print(f'valores: {v}')