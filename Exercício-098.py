# Faça um programa que tenha uma função chamada contador() que receba
# 3 parâmetros: início, fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens a partir da função criada:
# a) De 1 até 10, de 1 em 1.
# b) De 10 até 0, de 2 em 2.
# c) Uma contagem personalizada.
from time import sleep

def contador(i, f, p):
        if p < 0:
            p *= -1
        if p == 0:
            p = 1
        titulo(i, f, p)
        if i < f:
            cont = i
            while cont <= f:
                print(f'{cont} ', end='', flush=True)
                cont += p
                sleep(.2)
            print()
        print()
        if i > f:
            cont = i
            while cont >= f:
                print(f'{cont} ', end='', flush=True)
                cont -= p
                sleep(.2)
            print()
        print()
def titulo(i, f, p):
        print('-='*20)
        print(f'Contando de {i} até {f} de {p} em {p}.')
        print('-='*20)

#Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora defina a sua contagem personalizada:  ')
i = int(input('Digite o início:  '))
f  = int(input('Digite o fim:    '))
p = int(input('Digite o passo:   '))
print()
contador(i, f, p)
