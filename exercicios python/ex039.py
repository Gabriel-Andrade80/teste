from datetime import date
ano = int(input('ano: '))
idade = date.today().year - ano 
if idade < 18:
    print(f'voce tem {idade} anos, ainda irá se alistar')
elif idade == 18:
    print(f'voce tem {idade} anos, ta na hora de se alistar')
else:
    print(f'voce tem {idade} anos, ja passou do tempo de se alistar')
                
