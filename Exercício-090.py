#Faça um programa que leia nome e média de um aluno, guardando também
# a situação em um dicionário. No final, mostre o conteúdo da estrutura na
# tela.

lista = list()
cadastro = dict()

cadastro['Nome'] = str(input('Digite o nome do Aluno:  ')).capitalize()
cadastro['Média'] = float(input('Digite a média do Aluno:  '))
if cadastro['Média'] < 7:
    cadastro['Situação'] = 'Reprovado'
else:
    cadastro['Situação'] = 'Aprovado'
lista.append(cadastro.copy())

for k, v in cadastro.items():
    print(f'{k} é {v}')
