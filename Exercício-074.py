'''Crie um programa que gere 5 números aleátórios e coloque em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor
e o maior valor que estão na tupla.'''

from random import randint

numeros = (randint(1,100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
print('\033[1;31mOs números sorteados foram: ', end= '')
for c in numeros:
    print(f'{c} ', end= '')
print('\nO maior número sorteado foi {}'.format(max(numeros)))
print('O menor número sorteado foi {}'.format(min(numeros)))