n1 = int(input('n1: '))
n2 = int(input('n2: '))
n3 = int(input('n3: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('o maior é',maior)
print('o menor é',menor)