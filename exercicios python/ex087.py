matriz = []
for i in range(3):
    matriz.append([None] * 3)
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f'numero para [{[i]},{[j]}]: '))
for i in range(3):
    for j in range(3):
        print(f'{matriz[i][j]:^3}',end='  ')
    print()

soma = terc = 0
maior = matriz[1][0]
for i in range(3):
    for j in range(3):
        soma = soma + matriz[i][j] if matriz[i][j] % 2 == 0 else soma
        terc = terc + matriz[i][j] if j == 2 else terc
        if i == 1:
            if matriz[i][j] >= maior:
                maior = matriz[i][j]

print(f'A soma dos valores pares: {soma}')
print(f'A soma dos valores da terceira coluna: {terc}')
print(f'O maior valor da segunda linha: {maior}')