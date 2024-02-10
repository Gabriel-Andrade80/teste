num = int(input('quantos termos? '))
c = 0
n1 = 0
n2 = 1
print(n1,'-',n2,end='')
while c < num-2:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(' -',n3,end='')
    c += 1