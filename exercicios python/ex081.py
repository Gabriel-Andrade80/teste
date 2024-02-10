numeros = []
# c = 0
while True:
    # num = int(input('digite um valor: '))
    numeros.append(int(input('digite um valor: ')))
    # c += 1
    # if num == 5:
    #     val5 = True
    # else:
    #     val5 = False
    resp = input('Quer continuar [S/N]? ').upper().strip()[0]
    if resp == 'N':
        break
numeros.sort(reverse=True)
print(f'Voce digitou {len(numeros)} elementos.')
print(f'Ordem decrescente: {numeros}')
if 5 in numeros: # if val5 == True:
    print('O número 5 está na lista!')
else:
    print('O número 5 não foi encontrado.')
