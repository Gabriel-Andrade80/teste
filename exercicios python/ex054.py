ma = me = 0
for i in range(1,8):
    ano = int(input(f'ano de nascimento da {i}º pessoa: '))
    idade = 2023 - ano
    if idade < 18:
        me += 1
    else:
        ma += 1
print(f'{ma} pessoas maiores de 18 anos\n{me} pessoas menores de 18 anos')
    
