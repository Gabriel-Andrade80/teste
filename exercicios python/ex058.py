from random import randint
pc = randint(0,10)
user = int(input('Digite um valor: '))
tent = 1
while user != pc:
    if user < pc:
        print('Mais... tente denovo:')
    else:
        print('Menos... tente denovo:')
    user = int(input(''))
    tent += 1
print(f'Parabens, voce acertou em {tent} tentativa(s)!')
print(pc, user)