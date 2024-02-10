n = int(input('numero: '))
for i in range(1,11):
    m = n * i
    if n < 10:
        print(f'{n} x {i:2} = {m:2}')
    else:
        print(f'{n} x {i:2} = {m:3}')
