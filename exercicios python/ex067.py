while True:
    num = int(input('numero (digite negativo para sair): '))
    if num < 0:
        break
    for i in range(1,11):
        print(f'{num} x {i} = {num*i}')
    print('—'*40)
print('programa encerrado.')
