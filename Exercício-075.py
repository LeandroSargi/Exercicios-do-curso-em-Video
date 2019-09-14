'''Desenvolva um programa que leia 4 valores pelo teclado e salve-os em uma tupla.
No final mostre quantas vezes aparece o numero nove.
Em que posição foi mostrado o primeiro valor 3.
E quais foram os números pares.'''

print('\033[1;32mBem vindo ao programa inteligente!!')
condição = ''

numeros = (int(input('Digite o valor do primeiro número:  ')), int(input('Digite o valor do segundo número:  ')),
           int(input('Digite o valor do terceiro número:  ')), int(input('Digite o valor do quarto número:  ')))

print('Os numeros digitados foram:  ', end= '')

for n in numeros:
    print(f'{n} ', end= '')

print(f'\nO numero 9 aparece {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O primeiro numero 3 apareceu na posição {numeros.index(3)+1}.')
else:
    print('O número 3 não aparece na listagem.')

print('Os números pares foram:  ', end= '')

for n in numeros:
    if n % 2 == 0:
        condição = True

if condição == True:
    for n in numeros:
        if n % 2 == 0:
            print(f'{n} ', end='')
else:
    print('NENHUM')


