palavras = ('aprender','programar','linguagem','python','curso','gratis','estudar','praticar','trabalhar','mercado','programador','futuro')
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos:',end=' ')
    for i in palavra:
        if i.lower() in 'aeiou':
            print(i,end=' ')