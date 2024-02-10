numeros = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    num = int(input('Número de 0 a 20: '))
    if num not in range(0,21):
        print('numero inválido, tente novamente.',end=' ')
        continue
    else:
        print(f'Você digitou o número {numeros[num]}')
        break