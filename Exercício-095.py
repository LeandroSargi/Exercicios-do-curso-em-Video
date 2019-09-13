# Aprimore o desafio 093 para que funcione com vários jogadores, incluindo
# um sistema de visualização de detalhes do aproveitamento de cada jogador

gols = list()
campeonato = dict()
time = list()

print('-='*20)
print('{:^30}'.format('Aproveitamento de jogadores'))
print('-='*20)

while True:
    campeonato.clear()
    gols.clear()
    campeonato = {'Nome do Jogador': str(input('Digite o nome do jogador:  '))}
    partidas = int(input(f'Partidas que {campeonato["Nome do Jogador"]} jogou:  '))

    for c in range (0, partidas):
        gols.append(int(input(f'Gols feitos na partida {c+1}:  ')))

    campeonato['Gols Feitos'] =  gols[:]
    campeonato['Total de Gols'] = sum(gols)
    time.append(campeonato.copy())

    while True:
        opção = str(input('Deseja continuar? [S / N]:  ')).strip().upper()[0]
        if opção in 'SN':
            break
        print('ERRO!! Por favor, digite apenas S ou N.')
    if opção in 'N':
        break

print('-'*70)
print('cód.', end='')
for i in campeonato.keys():
    print(f'{i:<20}', end='')
print()
print('-'*70)

for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<20}', end='')
    print()
print('-'*60)
while True:
    resp = int(input('Você deseja exibir os dados de qual jogador? [999 PARA]:'))
    if resp == 999:
        break
    if resp >= len(time):
        print(f'ERRO!! Não existe jogador com o código {resp}')
    else:
        print(f'Mostrando dados do Jogador {time[resp]["Nome do Jogador"]}: ')
        for i, g in enumerate(time[resp]["Gols Feitos"]):
            print(f'        ==> Na partida {i+1} fez {g} gols.')
    print('-'*60)
print('>>> Volte Sempre <<<')
