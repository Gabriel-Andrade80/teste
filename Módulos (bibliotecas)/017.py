from math import hypot
ca = float(input('tamanho do cateto adjacente: '))
co = float(input('tamanho do cateto oposto: '))
hi = hypot(ca,co)
print('a hipotenusa é: {:.2f}'.format(hi))