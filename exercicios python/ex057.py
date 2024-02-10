sex = input('sexo [M/F]: ').upper()[0]
while sex != 'M' and sex != 'F':
    print('Inválido, por favor digite o valor correto.')
    sex = input('sexo [M/F]: ').upper()[0]
print(f'Sexo {sex} registrado.')