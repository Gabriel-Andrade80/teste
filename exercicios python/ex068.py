from random import randint
win = 0
while True:
    escolha = input('impar ou par (I/P): ').upper()[0]
    if escolha not in 'IP':
        print('Inválido, digite novamente.')
        continue
    num = int(input('digite um numero: '))
    pc = randint(0,10)
    soma = num + pc
    print(f'Voce jogou {num} e o computador {pc}, resultando no total {soma}.',end=' ')
    #resultado = 'P' if soma % 2 == 0 else resultado'I'
    if soma % 2 == 0:
        resultado = 'P'
        print(f'Resultado: PAR')
    else:
        resultado = 'I'
        print(f'Resultado: IMPAR')
    
    if resultado == escolha:
        print('_'*30)
        print('Voce venceu!!!\nVamos jogar novamente...')
        win += 1
        print('_'*30)
    else:
        print(f'Voce perdeu...\nAcumulou {win} vitória(s)!')
        break
