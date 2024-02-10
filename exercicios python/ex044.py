val = float(input('valor: R$'))
print('formato de pagamento:\n0 - dinheiro/cheque\n1 - à vista cartão\n2 - 2x no cartão\n3 - 3x ou mais no cartão')
n = int(input())
if n == 0:
    tot = val - (val * 0.1)
    print(f'valor: {tot}')
elif n == 1:
    tot = val - (val * 0.05)
    print(f'valor: {tot}')
elif n == 2:
    tot = val
    print(f'valor: {tot}')
elif n == 3:
    par = int(input('quantidade de parcelas: '))
    #tot = val * (1 + 0.2)**par juros composto ai
    tot = val + (val * 0.2)
    print(f'valor: {tot}')
else:
    print('numero inválido')
