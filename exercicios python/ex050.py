s = c = 0
for i in range(1,7):
    n = int(input(f'numero {i}: '))
    if n % 2 == 0:
        s += n
        c += 1
print(f'total dos {c} nº pares digitados: {s}')
