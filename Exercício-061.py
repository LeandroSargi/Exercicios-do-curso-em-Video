#Faça um programa que mostre os dez primeiros termos de uma progressão aritmética.
#Usando a estrutura de repetição while
print('Gerador de PA')
print('-='*10)
pt = int(input('Digite o Primeiro Termo da PA:\n'))
r = int(input('Digite a Razão da PA:\n'))
termo = pt
cont = 1

while cont <= 10:
    print('{} --> '.format(termo), end = '')
    termo += r
    cont += 1
print('FIM')
