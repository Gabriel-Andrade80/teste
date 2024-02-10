frase = input('frase: ').upper().strip().split()
nf = f = ''
f = ''.join(frase)
#for i in frase:
#    f += i 
for i in range(1,len(f) + 1):
    nf +=  f[-i]
print(f'{f}\n{nf}')
if nf == f:
    print('\nPALINDROMOOOOOOOO')
else:
    print('é nada n')
