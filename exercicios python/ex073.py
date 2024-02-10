times = ('Botafogo','Flamengo','Fluminense','Palmeiras','Bragantino','Grêmio','Athletico-PR','Cuiabá','São Paulo','Atlético-MG','Cruzeiro','Internacional','Fortaleza','Corinthians','Goiás','Bahia','Santos','Coritiba','Vasco da Gama','América-MG')
print('Times:',end=' ')
for i in times:
    if i == times[-1]:
        print(i)
    else:
        print(i,end=' - ')
print('')
print(f'5 primeiros: {times[:5]}\n')
print(f'4 últimos: {times[-4:]}\n')
print(f'ordem alfabetica: {sorted(times)}\n')
print(f'Vasco da Gama está na {times.index("Vasco da Gama")+1}º posição')
