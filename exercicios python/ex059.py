n1 = int(input('numero 1: '))
n2 = int(input('numero 2: '))
while True:
    print("=-=" * 10)
    num = int(input('[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair do programa\n'))
    if num == 1:
        soma = n1 + n2
        print('a soma dos numeros {} e {} é igual a {}'.format(n1,n2,soma))
    elif num == 2:
        mult = n1 * n2
        print('o produto dos numeros {} e {} é igual a {}'.format(n1,n2,mult))
    elif num == 3:
        maior = n1
        if n2 > n1:
            maior = n2
        print('o maior numero é {}'.format(maior))
    elif num == 4:
        n1 = int(input('numero 1: '))
        n2 = int(input('numero 2: '))
    elif num == 5:
        print('SAINDO...')
        break
    else:
        print('numeros válidos apenas de 1 a 5, digite novamente.')