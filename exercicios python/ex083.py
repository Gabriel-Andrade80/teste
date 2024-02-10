# exp = input('Digite a expressão: ')
# a = f = 0
# for p in exp:
#     if p == '(':
#         a += 1
#     elif p == ')':
#         f += 1
# if a == f:
#     print("Sua expressão é valida")
# else:
#     print("Sua expressão está errada!")
exp = input('Digite a expressão: ')
pilha = []
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('valido')
else:
    print('inválido')