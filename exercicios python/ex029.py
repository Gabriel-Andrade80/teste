vel = int(input('velocidade: '))
if vel > 80:
    t = vel - 80
    multa = t * 7
    print(f'Voce foi multado. Sua multa é de R$ {multa:.2f}')
else:
    print('dentro do limite')