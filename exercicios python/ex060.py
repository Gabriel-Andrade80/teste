num = int(input('numero: '))
fat = 1
print(f'{num}! =',end=' ')
while num > 0:
    fat *= num
    if num == 1:
        print(f'{num} =',end=' ')
    else:
        print(f'{num} x',end=' ')
    num -= 1
print(fat)