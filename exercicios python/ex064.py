tot = c = 0
while True:
    num = int(input('numero [999 para sair]: '))
    if num == 999:
        break
    else:
        tot += num
        c += 1
print('quant de numeros digitados: {}'.format(c))
print('soma dos numeros: {}'.format(tot))