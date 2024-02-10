num = input('digite um numero: ')
for i in range(len(num)-1,-1,-1):
    if i == 3:
        print('unidade:',num[-1])
    if i == 2:
        print('dezena:',num[-2])
    if i == 1:
        print('centena:',num[-3])
    if i == 0:
        print('milhar:',num[-4])