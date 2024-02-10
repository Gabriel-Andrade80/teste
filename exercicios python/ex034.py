sal = float(input('salario: R$'))
if sal > 1250.00:
    sal += sal * 0.1 #sal = sal + sal * 0,1
else:
    sal += sal * 0.15
print('seu novo salario é R$ {:.2f}'.format(sal))