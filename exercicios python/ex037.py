num = int(input('numero: '))
print('qual é a base de conversao?')
print('1 p/ binario, 2 p/ octal, 3 p/ hexadecimal)')
base = int(input())
if base == 1:
    print(bin(num))
    print(f'{num:b}')
    print(format(num, 'b'))
elif base == 2:
    print(oct(num))
    print(f'{num:o}')
    print(format(num, 'o'))
elif base == 3:
    print(hex(num))
    print(f'{num:x}')
    print(format(num, 'x'))
else:
    print('numero inválido')
