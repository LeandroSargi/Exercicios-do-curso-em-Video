'''Aprimore o desafio anterior, mostrando no final.
A soma de todos os valores pares digitados.
A soma dos valores da terceira coluna.
O maior valor da segunda linha'''

lista =  []
dados = []
soma = 0
somalinha = 0
maior = 0
count = 0

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
    if lista.index(item) == 1:
        while count < len(item):
            somalinha += item[count]
            if count == 0:
                maior = item[count]
            else:
                if item[count] > maior:
                    maior = item[count]
            count += 1
    for n in item:
        if n % 2 == 0:
            soma += n
        print(f'{[ n ]}', end = '')
    print('\n', end = '')

print(f'A soma dos valores pares é {soma}.')
print(f'A soma dos itens da segunda linha é {somalinha}.')
print(f'O maior valor da segunda linha é {maior}.')

