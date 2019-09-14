print('Olá bem vindo ao programa que separa números maiores e menores!!')
n1 = int(input('Por favor, digite o primeiro número:\n'))
n2 = int(input('Digite o segundo número:\n'))
n3 = int(input('Agora digite o terceiro número:\n'))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor número é {} e o maior número é {}.'.format (menor, maior))