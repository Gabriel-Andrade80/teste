from random import randint
v = []

for i in range(5):
    v.append(randint(0,10))

v = tuple(v)

print('Os valores sorteados foram:',end=' ')

maior = menor = v[0]
for num in v:
    print(num,end=' ')
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print(f'\nO maior valor sorteado foi {maior}') #max(v)
print(f'O menor valor sorteado foi {menor}') #min(v)