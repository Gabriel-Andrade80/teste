import random
v = []
v.append(input('primeiro aluno: '))
v.append(input('segundo aluno: '))
v.append(input('terceiro aluno: '))
v.append(input('quarto aluno: '))
al = random.choice(v)
print('o aluno escolhido foi', al)