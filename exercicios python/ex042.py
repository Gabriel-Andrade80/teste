A = int(input('lado 1: '))
B = int(input('lado 2: '))
C = int(input('lado 3: '))
AB = abs(A - B)
AC = abs(A - C)
BC = abs(B - C)
#if A < B + C and B < A + C and C < A + B:
if (A > BC and A < B + C) and (B > AC and B < A + C) and (C > AB and C < A + B):
    if A == B == C:
        print('TRIÂNGULO EQUILÁTERO!')
    elif (A == B and B != C) or (A == C and A != B) or (B == C and C != A): #perca de tempo, era so fazer o escaleno antes desse e meter um else 
        print('TRIÂNGULO ISÓCELES!')
    elif A != B != C:
        print('TRIÂNGULO ESCALENO!')
    
else:
    print('NÃO!')
