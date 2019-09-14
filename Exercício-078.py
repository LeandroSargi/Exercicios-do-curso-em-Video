'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado.
E as suas posições na lista.'''

numeros = [int(input('\033[1;35mDigite um número para a posição 1: ')), int(input('Digite um número para a posição 2: ')),
           int(input('Digite um número para a posição 3: ')), int(input('Digite um número para a posição 4: ')),
           int(input('Digite um número para a posição 5: '))]


print(f'O maior número digitado foi {max(numeros)} na posição {numeros.index(max(numeros))+1}.')
print(f'O menor número digitado foi {min(numeros)} na posição {numeros.index(min(numeros))+1}.')
