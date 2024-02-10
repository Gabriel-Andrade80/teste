print('-'*40)
print(' '*11,'LOJA SUPER BARATÃO',' '*11)
print('-'*40)
total = totmil = c = menor = 0
while True:
    produto = input('produto: ')
    preco = float(input('preço: R$'))
    c += 1
    if c == 1 or preco < menor:
        menor = preco
        barato = produto
    if preco > 1000:
        totmil += 1
    total += preco
    nome = ' '
    while nome not in 'SN':
        nome = input('quer continuar? [S/N] ').upper().strip()[0]
    if nome == 'N':
        break
print(f'total da compra: R${total:.2f}\nTemos {totmil} produtos acima de R$1000.00\nO produto mais barato foi {barato}, custando R${menor:.2f}')
