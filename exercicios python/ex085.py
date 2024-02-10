numeros = []
for i in range(2):
    numeros.append([])
for i in range(7):
    num = (int(input(f'{i+1}º numero: ')))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)    
numeros[0].sort()
numeros[1].sort()
print(f'valores pares: {numeros[0]}\nvalores ímpares: {numeros[1]}')