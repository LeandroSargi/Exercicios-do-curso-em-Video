'''Crie um programa que crie uma matriz de dimensão 3x3 e preencha
com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.'''

lista =  []
dados = []
linha = []


for c in range(0,3):
    dados.append(int(input('Digite um valor para a linha 1:  ')))
    linha.append(dados[:])
    dados.clear()
    
lista.append(linha[:])
linha.clear()

for c in range(0,3):
    dados.append(int(input('Digite um valor para a linha 2:  ')))
    linha.append(dados[:])
    dados.clear()
    
lista.append(linha[:])
linha.clear()

for c in range(0,3):
    dados.append(int(input('Digite um valor para a linha 3:  ')))
    linha.append(dados[:])
    dados.clear()

lista.append(linha[:])
linha.clear()

for n in lista:
    for item in n:
        print(item, end = '')
    print('\n', end = '')
