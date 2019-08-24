# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando
# os dados de cada pessoa em um dicionário e todos os dicionários em uma
# lista. No final, mostre:
# a) Quantas pessoas foram cadastradas
# b) A média de idade do grupo
# c) Uma lista com todas as mulheres
# d) Uma lista com todas as pessoas com idade acima da média

cadastro = dict()
from operator import itemgetter
lista = list()
opção = ''
soma = média = 0

while True:
    cadastro.clear()
    cadastro['Nome'] = str(input('Digite o nome:  ')).capitalize()
    cadastro['Sexo'] = str(input('Digite o sexo [M / F]:  ')).upper()[0]
    cadastro['Idade'] = int(input('Digite a idade:  '))
    soma += cadastro['Idade']
    lista.append(cadastro.copy())
    while True:
        opção = str(input('Deseja continuar? [S / N]:  ')).strip() .upper() [0]
        if opção in 'SN':
            break
        print('ERRO!! Por favor, digite apenas S ou N.')
    if opção == 'N':
        break
média = soma // len(lista)

print(f'Ao todo foram cadastradas {len(lista)} pessoas.')
print(f'A média de idade do grupo é de {média:5.2f} anos.')
print('As mulheres cadastradas foram ', end= '')
for p in lista:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]} ', end= '')
print()
print('As pessoas com idade acima da média foram:')
for p in lista:
    if p['Idade'] >= média:
        for k, v in p.items():
            print(f'{k} >> {v}. ', end= '')
        print()
