frase = input('frase: ').strip().upper()
print("Quantos 'A'? {}".format(frase.count('A')))
print('onde aparece pela 1º vez? {}'.format(frase.find('A')))
print('onde aparece pela última vez? {}'.format(frase.rfind('A')))