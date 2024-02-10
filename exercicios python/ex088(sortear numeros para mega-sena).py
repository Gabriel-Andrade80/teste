from random import randint
from time import sleep
print('-'*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-'*30)
num = int(input('quantos jogos serão gerados? '))
v = []
for i in range(num):
    v.append([None] * 6)

for i in range(num):
    j = 0
    while j < 6:
        valor = randint(1,60)
        if valor not in v[i]: 
            v[i][j] = valor
        else:
            continue       
        j += 1
    v[i].sort()
print(f'-=-=-= SORTEANDO {num} JOGOS -=-=-=')
for i,c in enumerate(v):
    print(f'jogo {i+1}: {c}')
    sleep(1)