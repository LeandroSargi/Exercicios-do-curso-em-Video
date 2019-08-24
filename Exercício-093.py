# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total de gols feitos
# durante o campeonato.
gols = list()

print('-='*20)
print('{:^30}'.format('Aproveitamento de jogadores'))
print('-='*20)

campeonato = {'Nome do Jogador': str(input('Digite o nome do jogador:  '))}
partidas = int(input(f'Partidas que {campeonato["Nome do Jogador"]} jogou:  '))

for c in range (0, partidas):
    gols.append(int(input(f'Gols feitos na partida {c+1}:  ')))

campeonato['Gols Feitos'] =  gols[:]
campeonato['Total de Gols'] = sum(gols)

print('-='*20)
print(campeonato)
print('-='*20)
print(f'Nome do jogador é {campeonato["Nome do Jogador"]}.')
print(f'{campeonato["Nome do Jogador"]} jogou {partidas} partidas.')
for c, g in enumerate(gols):
    print(f'        ==> Na partida {c+1} fez {g} gols.')
print('-='*20)
