m18 = homem = mulher20 = 0
while True:
    sexo = ''
    idade = int(input('idade: '))
    while sexo not in 'MF':
        sexo = input('sexo [M/F]: ').strip().upper()[0]
    if idade > 18:
        m18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    resp = ''
    while resp not in 'SN':
        resp = input('Quer continuar [S/N]? ').upper()[0]
    if resp == 'N':
        print('Saindo...')
        print('-'*40)
        break
    print('-'*40)
print(f'Acima de 18: {m18} pessoas\nQuantidade de homens: {homem} homens\nMulheres abaixo de 20: {mulher20} mulheres')
