from random import choice
print('Bem vindo ao programa de sorteio de nomes!!')
n1 = str(input('Digite o primeiro nome:\n'))
n2 = str(input('Digite o segundo nome:\n'))
n3 = str(input('Digite o terceiro nome:\n'))
n4 = str(input('Digite o quarto nome:\n'))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O escolhido é {}'.format(escolhido))