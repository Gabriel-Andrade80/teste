v = []
while True:
    num = int(input('digite um valor: '))
    if num not in v:
        v.append(num)
    else:
        print(f'valor duplicado. Impossível adicionar.')
    resp = input('Quer continuar [S/N]? ').upper().strip()[0]
    if resp == 'N':
        break
b = v[:]
b.sort()
print(f'Valores digitados: {v}\nOrdem crescente: {b}')
