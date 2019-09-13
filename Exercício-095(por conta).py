# 093 - Crie um programa que gerencie o aproveitamento de um jogador de
# futebol. O programa vai ler o nome de jogador e quantas partidas ele
# jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o
# total de gols feitos durante o campeonato.

# 095 - Aprimore o desafio 093 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes de aproveitamento de
# cada jogador.

ficha = dict()
gols = []
time = list()


print('\033[30;43m-'*50)
print(f'{"Aproveitamento de Jogadores":^50}')
print('-'*50)
print('\033[m', end='')
while True:
    ficha.clear()
    gols.clear()
    resp = ''
    ficha['Nome Jogador'] = str(input('Digite o nome do jogador(a):  ')).upper()
    ficha['Partidas'] = int(input(f'Digite quantas partidas {ficha["Nome Jogador"]} jogou:  '))
    for c in range(0, (ficha['Partidas'])):
        gols.append(int(input(f'Gols feitos na partida {c+1}:  ')))
    ficha['Gols'] = gols[:]
    ficha['Total de Gols'] = sum(gols)
    time.append(ficha.copy())
    while True:
        resp = str(input('Quer adicionar mais jogadores [SIM / NÃO]?  ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('\033[1;31m Erro!! Por favor digite apenas SIM ou NÃO!\033[m')
    if resp in 'N':
        break

print('\033[30;43m-'*50)
print(f'{"TABELA":^50}')
print('-'*50)
print('\033[m', end='')

print('\033[30;41mcod. ', end='')
for i in ficha.keys():
    print(f'| {i:<20}', end='')
print('\033[m')

for k, v in enumerate(time):
    print(f'\033[7;30m{k:>5}', end='')
    for d in v.values():
        print(f'| {str(d):<20}', end='')
    print('\033[m')

while True:
    resp = ''
    resp = str(input('Digite o código do jogador para resultados [999 PARA]:'))
    if resp.isnumeric():
        resp = int(resp)
        if resp == 999:
            break
        if resp >= len(time):
            print(f'Erro!! Não temos jogador com o código {resp}.')
        else:
            print('\033[30;43m-'*50)
            print(f'{time[resp]["Nome Jogador"]:^50}')
            print('-' * 50)
            print('\033[m', end='')
            for i, g in enumerate(time[resp]["Gols"]):
                print(f'\033[7;30m   ---> Na partida {i+1} fez {g} gol(s)\033[m')
    else:
        print('Erro!! Por favor digite um código válido!')
print('>>> FINALIZANDO <<<')


