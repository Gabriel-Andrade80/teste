n1 = float(input('nota: '))
n2 = float(input('nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('reprovado')
elif media >= 5 and media <= 6.99:
    print('recuperation')
else:
    print('aprovado')
