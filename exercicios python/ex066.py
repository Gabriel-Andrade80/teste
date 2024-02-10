c = s = 0
while True:
    num = int(input('numero: (digite 999 para sair) '))
    if num ==  999:
        break
    c += 1
    s += num
print(f'quantidade: {c}\nsoma: {s}')
