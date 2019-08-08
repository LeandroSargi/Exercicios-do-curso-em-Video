'''Crie um programa que leia nome e duas notas de vários alunos e
guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita
que o usuário possa mostrar as notas cada aluno individualmente.'''

dados = list()
lista = list()
resposta = ''
opção = 0

while True:
    dados.append(str(input('Digite o nome:  ')).capitalize())
    dados.append(float(input('Digite a primeira nota:  ')))
    dados.append(float(input('Digite a segunda nota:  ')))
    resposta = str(input('Deseja continuar? [S/N] ')).strip() .upper() [0]
    lista.append(dados[:])
    dados.clear()
    if resposta in 'N':
        break

for c in lista:
    print(f'{lista.index(c)} - Nome:  {lista[lista.index(c)][0]} -------------- Média:  {((lista[lista.index(c)][1] + lista[lista.index(c)][2])/2)}')

while opção != 999:
    opção = int(input('Digite o número do aluno do qual deseja saber as notas [999 para parar]:  '))
    if opção == 999:
        print('Finalizando.....')
        break
    for c, item in enumerate(lista):
        if opção == c:
            print(f'Aluno {lista[opção][0]} >>>>>>>>> Nota 1: {lista[opção][1]} >>>>>>>> Nota 2: {lista[opção][2]}')
            break

