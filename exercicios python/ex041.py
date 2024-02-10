ano = int(input('ano: '))
ano = 2023 - ano
print('idade: {}'.format(ano))
if ano <= 9:
    print('MIRIM')
elif ano > 9 and ano <= 14:
    print('INFANTIL')
elif ano > 14 and ano <= 19:
    print('JUNIOR')
elif ano > 19 and ano <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
