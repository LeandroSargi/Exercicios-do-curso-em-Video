# Faça um programa que tenha uma lista chamada números e duas funções
# chamadas sorteia() e somapar(). A primeira função vai sortear 5 números
# e vai colocá-los dentro da lista e a segunda função vai mostrar a
# soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep
lista = []


def sorteia():
    for c in range(0,5):
        lista.append(randint(0,100))

def somapar():
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'A soma dos números pares é {soma}.')

#Programa principal
sorteia()
print('Os números sorteados foram: ', end= '')
for n in lista:
    print(f'{n} ', end= '', flush=True)
    sleep(.3)
print()
somapar()
