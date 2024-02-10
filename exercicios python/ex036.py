valor = float(input('valor da casa: R$'))
sal = float(input('salario: R$'))
anos = int(input('quantos anos: '))
prestacao = valor / (anos * 12)
limite = sal * 0.3
if prestacao > limite:
    print('EMPRÉSTIMO NAO APROVADO!')
else:
    print('APROVADO!')
