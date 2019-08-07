'''Crie um programa que leia nome e duas notas de vários alunos e
guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita
que o usuário possa mostrar as notas cada aluno individualmente.'''

dados = list()
lista = list()
resposta = ''

while True:
    dados.append(str(input('Digite o nome:  ')))
    dados.append(float(input('Digite a primeira nota:  ')))
    dados.append(float(input('Digite a segunda nota:  ')))
    resposta = str(input('Deseja continuar? [S/N] ')).strip() .upper() [0]
    lista.append(dados[:])
    dados.clear()
    if resposta in 'N':
        break

#for c in range(0, (len(lista)+1)):
#    for d in lista[c]:
#        print(d[d])
#    print(lista[c])



#    for d in lista:
#        print(f'Nome:  {lista[0][0]}')
#        print(f'Média: {lista[0][1]/lista[0][2]} ')
