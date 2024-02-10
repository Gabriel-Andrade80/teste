num = int(input('numero: '))
#if (num % 4 == 0) and (num % 100 != 0) or num % 400 == 0: 
if (num % 4 == 0) and (num % 100 != 0): 
    print('BISSEXTO!')
elif (num % 100 == 0) and (num % 400 == 0):
    print('BISSEXTO')
else:
    print('FALSO!')
