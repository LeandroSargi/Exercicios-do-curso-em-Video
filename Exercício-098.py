# Faça um programa que tenha uma função chamada contador() que receba
# 3 parâmetros: início, fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens a partir da função criada:
# a) De 1 até 10, de 1 em 1.
# b) De 10 até 0, de 2 em 2.
# c) Uma contagem personalizada.
from time import sleep

def contador():
    if opção == 1:
        for c in range(1,11):
            print(c)
            sleep(.8)
    if opção == 2:
        for c in range(10, -1, -2):
            print(c)
            sleep(.8)
    if opção == 3:
        início = int(input('Digite o número de início da contagem:  '))
        fim = int(input('Digite o número de término da contagem:  '))
        passo = int(input('Digite o passo da contagem:  '))
        if passo == 0:
            passo = 1
        if início > fim:
            passo = passo - (passo*2)

        for c in range(início, fim+passo, passo):
            print(c)
            sleep(.8)


print('1 - Para contar de 1 até 10 de 1 em 1')
print('2 - Para contar de 10 até 0 de 2 em 2')
print('3 - Para configurar uma contagem personalizada')

opção = int(input('Digite a opção desejada:  '))

contador()
