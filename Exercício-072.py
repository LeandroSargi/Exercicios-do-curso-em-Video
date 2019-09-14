'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
por extenso de zero até 20.
Seu programa deverá ler um número pelo teclado (entre zero e vinte) e mostrá-lo
por extenso.'''

contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
            'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True: #repetição infinita
    numero = int(input('Digite um número entre 0 e 20: ')) #entrada
    if 0 <= numero <= 20: #se o numero digitado for maior/igual zero e menor/igual vinte
        break #pare
    print('Você não digitou um número entre 0 e 20, tente novamente.', end = '') #validação de entrada
print(f'Você digitou o número {contagem[numero]}.') #imprime o numero digitado com seu respectivo extenso
