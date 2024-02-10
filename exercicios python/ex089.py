v = []
media = []
while True:
    nome = input('Nome: ')
    not1 = float(input('Nota 1: '))
    not2 = float(input('Nota 2: '))
    v.append([nome,not1,not2])
    resp = input(f'Quer continuar? [N/S] ').upper().strip()[0]
    if resp == 'N':
        break
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i,l in enumerate(v):
    media.append((l[1] + l[2]) / 2)
    print(f'{i:<4}{l[0]:<10}{media[i]:>8.1f}')
while True:
    print('-'*26)
    num = int(input('de qual aluno deseja mostrar as notas? [999 interrompe]: '))
    if num == 999:
        break
    print(f'notas de {v[num][0]}: [{v[num][1]}, {v[num][2]}]')

