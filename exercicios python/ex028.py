from random import randint
pc = randint(0,5)
num = int(input('qual numero eu pensei? '))
if num == pc:
    print('parabens, voce acertou!')
else:
    print('errou, eu pensei em {}'.format(pc))