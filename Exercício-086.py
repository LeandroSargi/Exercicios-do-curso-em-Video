'''Crie um programa que crie uma matriz de dimensão 3x3 e preencha
com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.'''

lista =  []
dados = []
linha1 = []
linha2 = []
linha3 = []

for c in range(0,3):
    dados.append(int(input('Digite um valor para a linha 1:  ')))
    linha1.append(dados[:])
    dados.clear()

for c in range(0,3):
    dados.append(int(input('Digite um valor para a linha 2:  ')))
    linha2.append(dados[:])
    dados.clear()

for c in range(0,3):
    dados.append(int(input('Digite um valor para a linha 3:  ')))
    linha3.append(dados[:])
    dados.clear()

print(linha1, linha2, linha3)

for n in linha1:
    print(n, end = '')
print('\n', end = '')
for n in linha2:
    print(n, end = '')
print('\n', end = '')
for n in linha3:
    print(n, end = '')
