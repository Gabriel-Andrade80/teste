dis = float(input('distancia: '))
#preco = dis * 0.5 if dis <= 200 else dis * 0.45
if dis <= 200:
    pre = dis * 0.5
else:
    pre = dis * 0.45
print('preço da viagem: {:.2f}'.format(pre))