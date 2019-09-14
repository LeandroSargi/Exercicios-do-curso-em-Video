'''Crie um programa que tenha uma tupla unica com produtos e seus respectivos preços
na sequencia.
No final, mostre uma listagem de preços, organizando os dados de forma tabular.'''

listagem = ('Borracha', 1.75, 'Lápis', 0.50, 'Transferidor', 3.50, 'Régua', 5.00, 'Tesoura', 4.50, 'Folha Sulfite', 25.00)

print('-'*40)
print('{:^40}'.format('Lista de Materiais'))
print('-'*40)
for n in range(0, len(listagem)):
    if n % 2 == 0:
        print(f'{listagem[n]:.<30}', end='')
    else:
        print(f'{listagem[n]:>10.2f}')
print('-'*40)