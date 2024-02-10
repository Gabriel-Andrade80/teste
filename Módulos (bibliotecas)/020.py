from random import shuffle
v = []
v.append(input('primeiro aluno: '))
v.append(input('segundo aluno: '))
v.append(input('terceiro aluno: '))
v.append(input('quarto aluno: '))
shuffle(v)
print('a ordem foi', v)