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
