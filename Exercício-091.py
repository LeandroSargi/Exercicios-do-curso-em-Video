# Crie um programa onde 4 jogadores joguem um dado e tenham resultados
# aleatórios. Guarde esses resultados em um dicionário, no final, coloque
# este dicionário em ordem, sabendo que o vencedor tirou o maior número no
# dado.
from random import randint
jogada = dict()


jogada['Jogador1'] = randint(1,6)
jogada['Jogador2'] = randint(1,6)
jogada['Jogador3'] = randint(1,6)
jogada['Jogador4'] = randint(1,6)

print(jogada)
