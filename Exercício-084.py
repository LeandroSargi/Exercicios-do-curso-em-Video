'''Faça um programa que leia o nome e peso de várias pessoas,
guardando tudo em uma lista. No final mostre:
Quantas pessoas foram cadastradas.
Uma listagem com as pessoas mais pesadas.
Uma listagem com as pessoas mais leves.'''

pessoas = []
dados = []
pesadas = []
leves = []
maior = menor = 0
c = 1

while True:
    dados.append(str(input(f'Digite o nome da {c}° pessoa:  ')).strip() .capitalize())
    dados.append(float(input(f'Digite o peso da {c}° pessoa:  ')))
    if len(pessoas) == 0:
            maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if menor > dados[1]:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    opção = str(input('Deseja continuar? [S / N]:  '))
    if opção in 'Nn':
        break
    c += 1

for p in pessoas:
    if p[1] == maior:
        pesadas.append(p[0])
    elif p[1] == menor:
        leves.append(p[0])

print(f'Você cadastrou {c} pessoas!')
print(f'As mais leves são: {leves}. Pesando {menor} quilos.')
print(f'As mais pesadas foram: {pesadas}. Pesando {maior} quilos.')
