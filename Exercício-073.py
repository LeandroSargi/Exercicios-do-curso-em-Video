'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato
brasileiro de futebol na ordem de colocação, depois mostre:
Apenas os cinco primeiros colocados, os ultimos 4 colocados da tabela,
uma lista com os times em ordem alfabetica, em que posição na tabela está
o time da Chapecoense.'''

tabela = ('Palmeiras', 'Santos', 'Flamengo', 'Internacional', 'Atlético', 'Goiás',
          'Botafogo', 'Bahia', 'São Paulo', 'Corinthians', 'Grêmio', 'Atlético-PR',
          'Ceará SC', 'Fortaleza', 'Vasco da Gama', 'Fluminense', 'Chapecoense',
          'Cruzeiro', 'CSA', 'Hawai')
print('\033[1;32mOs 5 primeiros colocados do Campeonato são:')
for c in range(0, 5):
    print(f'{tabela[c]}')
print('-='*20)

print('Os 4 últimos colocados da tabela são:')
for c in range (-1, -5, -1):
    print(f'{tabela[c]}')
print('-='*20)
print('Aqui estão todos os times em ordem alfabética:')
print(sorted(tabela))
print('-='*20)

print('O time da Chapeconese está na {}° posição.'.format(tabela.index('Chapecoense')+1))