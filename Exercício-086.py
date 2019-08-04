'''Crie um programa que crie uma matriz de dimensão 3x3 e preencha
com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.'''

lista =  []
dados = []
numeros = []


for c in range(0,3):
    dados.append(int(input('Digite um valor para a linha 1:  ')))
lista.append(dados[:])
dados.clear()

for c in range(0,3):
    dados.append(int(input('Digite um valor para a linha 2:  ')))
lista.append(dados[:])
dados.clear()

for c in range(0,3):
    dados.append(int(input('Digite um valor para a linha 3:  ')))
lista.append(dados[:])
dados.clear()

for item in lista:
    for n in item:
        print(f'{[ n ]}', end = '')
    print('\n', end = '')
