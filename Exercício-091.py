# Crie um programa onde 4 jogadores joguem um dado e tenham resultados
# aleatórios. Guarde esses resultados em um dicionário, no final, coloque
# este dicionário em ordem, sabendo que o vencedor tirou o maior número no
# dado.
from time import sleep
from random import randint
from operator import itemgetter #módulo para colocar dicionário em ordem
jogada = dict()
ranking = list()

jogada['Jogador1'] = randint(1,6)
jogada['Jogador2'] = randint(1,6)
jogada['Jogador3'] = randint(1,6)
jogada['Jogador4'] = randint(1,6)

print('-='*20)
print('{:^40}'.format('Sorteando'))
print('-='*20)

for k, v in jogada.items():
    print(f'O {k} tirou {v}')
    sleep(1)

print('-='*20)
print('Ranking dos jogadores:')

ranking = sorted(jogada.items(), key=itemgetter(1), reverse=True)
#Sorteando items da jogada, levando em consideração a chave 1 que são
# os valores dos dados, modo reverso verdadeiro

for i, v in enumerate(ranking):
    print(f'{i+1}° lugar >>> {v[0]} com {v[1]} pontos.')
