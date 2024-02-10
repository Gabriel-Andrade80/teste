par = []
numeros = []
impar = []
while True:
    numeros.append(int(input('digite um valor: ')))
    resp = input('Quer continuar [S/N]? ').upper().strip()[0]
    if resp == 'N':
        break
for num in numeros:
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
print(f'Números digitados: {numeros}')
print(f'Números pares: {par}')
print(f'Números ímpares: {impar}')
