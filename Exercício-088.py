'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6
números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
from random import randint
lista = []
dados = []
valor = 0
cont = 0
print('-'*50)
print('{:^50}'.format('Jogo da Mega Sena'))
print('-'*50)
palpites = int(input('Digite quantos palpites você deseja exibir?  '))
for c in range (0, palpites):
    for c in range(0, 6):
        valor = randint(1,60)
        if valor not in dados:
            dados.append(valor)
    while(len(dados)) <= 6:
        if len(dados) == 6:
            break
        valor = randint(1,60)
        if valor not in dados:
            dados.append(valor)
    lista.append(dados[:])
    dados.clear()
    valor = 0
print(lista)
for c in range(0, (len(lista))):
    print(f'Jogo {c+1} : {lista[c]}')
    
    
        
