totage = tot20 = ma = 0

for i in range(1,5):
    print(f'---------{i}º pessoa---------')
    name = input('nome: ')
    age = int(input('idade: '))
    sx = input('sexo (M/F): ').upper()
    if sx == 'M':
        if age > ma:
            maisvelho = name
            ma = age
    if sx == 'F':
        if age < 20:
            tot20 += 1
    totage += age
med = totage / 4
print(f'media do grupo: {med}\nHomem mais velho: {maisvelho} com {ma} anos')
print(f'Quant de mulheres < 20 anos: {tot20} mulheres')
