'''Crie um programa que leia uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a sua expressão está com os parênteses
abertos e fechados na ordem correta.'''

expressão = str(input('\033[1;32mDigite a sua expressão:  '))
if expressão.count('(') == (expressão.count(')')):
    print('Sua expressão está correta!!')
else:
    print('Sua expressão está incorreta.')