saque = int(input('qual valor a sacar? R$'))
valor = saque
if valor // 50 > 0:
    cinq = valor // 50
    print(f'Total de {cinq} notas de R$50')
    valor -= (50 * cinq)
if valor // 20 > 0:
    vinte = valor // 20
    print(f'Total de {vinte} notas de R$20')
    valor -= (20 * vinte)
if valor // 10 > 0:
    dez = valor // 10
    print(f'Total de {dez} notas de R$10')
    valor -= (10 * dez)
if valor // 1 > 0:
    um = valor // 1
    print(f'Total de {um} notas de R$1')
    valor -= (1 * um)
 