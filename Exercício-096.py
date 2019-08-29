#Faça um programa que tenha uma função chamada área(), que receba as
# dimensões de um terreno retangular (largura e comprimento) e mostre a
# área do terreno.

def área(x,y):
    área = x*y
    print(f'A área do terreno é {área:.2f}m²')

x = float(input('Digite a largura do terreno em m²:  '))
y = float(input('Digite o comprimento do terreno em m²:  '))
área(x, y)
