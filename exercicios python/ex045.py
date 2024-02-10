from random import randint
joke = ['pedra','papel','tesoura']
pc = randint(0,2)
eu = int(input('0 - pedra\n1 - papel\n2 - tesoura\n'))
if eu == 0: #pedra
    if pc == 0: #pedra
        print('empate')
    elif pc == 1: #papel
        print('PC WINS!')
    else: #tesoura
        print('USER WINS!')
elif eu == 1: #papel
    if pc == 0: #pedra
        print('USER WINS!')
    elif pc == 1: #papel
        print('empate')
    else: #tesoura
        print('PC WINS!')
elif eu == 2: #tesoura
    if pc == 0: #pedra
        print('PC WINS!')
    elif pc == 1: #papel
        print('USER WINS!')
    else: #tesoura
        print('empate')
else:
    print('resposta inválida')
print(f'\npc - {joke[pc]}\njogador - {joke[eu]}') 
