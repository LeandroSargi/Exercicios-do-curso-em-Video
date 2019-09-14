#Faça um programa que leia um número inteiro qualquer e mostre na tela o seu fatorial:

#solução professor

from math import factorial
n = int(input('Digite um número do qual deseja saber o fatorial:\n'))
f = factorial(n)
print('O fatorial de {} é {}!'.format(n, f))