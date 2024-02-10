v = []
for i in range(1,5):
    num = int(input(f'numero {i}º: '))
    v.append(num)
v = tuple(v)
print(f'Você digitou os valores {v}')
print(f'o número 9 aparece {v.count(9)} vezes')
if 3 in v:
    print(f'o valor 3 aparece na {v.index(3)+1}º posição')
else:
    print('o valor 3 não foi digitado.')
print('Os valores pares digitados foram:',end=' ')
for i in v:
    if i % 2 == 0:
        print(i,end=' ')
