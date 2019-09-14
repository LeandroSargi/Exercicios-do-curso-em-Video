'''Crie um programa que vai ler vários números e colocá-los em uma lista.
Depois disso, mostre.
Quantos números foram digitados.
A lista de valores ordenada de forma decrescente.
Se o valor 5 foi digitado e está ou não na lista.'''

numeros = list() #LISTA RECEBE VAZIO, POSSO TAMBÉM ESCREVER ASSIM: numeros = []

while True:
    valor = int(input(f'\033[1;35mDigite um valor:    ')) #ENTRADA DE VALOR
    numeros.append(valor) #LISTA RECEBE O VALOR DIGITADO
    opção = str(input('Quer continuar? [S/N]:   ')) .strip() .upper() [0]
    if opção in 'N': #SE A OPÇÃO FOR NÃO O PROGRAMA PARA
        break


print(f'Você digitou {len(numeros)} números, são eles: {numeros}.') #MOSTRA QUANTOS NUMEROS FORAM DIGITADOS E QUAIS
numeros.sort(reverse=True) #O COMANDO SORT COLOCA OS NUMEROS EM ORDEM CRESCENTE, E OS REVERTE ATRAVÉS DO REVERSE=TRUE
print(f'Os números em ordem decrescente ficam assim: {numeros}') #MOSTRA OS NUMEROS INVERTIDOS
if 5 in numeros: #O PYTHON CONSEGUE BUSCAR UM ITEM DENTRO DE UMA LISTA, SEM USAR LAÇOS
    print('O número 5 está nesta lista.') #MOSTRA RESULTADO
else:
    print('O número 5 não está na lista.')
