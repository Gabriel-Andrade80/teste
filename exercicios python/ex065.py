tot = c = 0
num = int(input('numero: '))
maior = menor = num
while True:
    tot += num
    c += 1
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    op = input('quer continuar [S/N]? ').upper()[0].strip()
    if op == 'N':
        break
    num = int(input('numero: '))
med = tot / c
print('quant de numeros digitados: {}'.format(c))
print('media dos numeros: {}'.format(med))
print('maior: {}\nmenor: {}'.format(maior,menor))