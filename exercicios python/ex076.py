produtos = ('Lápis',1.75,'Borracha',2.00,'Caderno',15.90,'Estojo',25.00,'Transferidor',4.20,'Compasso',9.90,'Mochila',120.32,'Canetas',22.30,'Livro',34.90)
print('-'*38)
print(f'{"LISTAGEM DE PREÇOS":^38}')
#print(' '*9,'LISTAGEM DE PREÇOS',' '*10)
print('-'*38)

for i in range(0,len(produtos),2):
    #forma = 29 - len(produtos[i])
    print(f'{produtos[i]:.<29}R$ {produtos[i+1]:>6.2f}') #{"."*forma}
print('-'*38)