# Crie um programa que leia nome, ano de nascimento e carteira de trabalho
# e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for
# diferente de zero, o dicionário receberá também o ano de contratação e o
# salário. Calcule e acrescente, além da idade, com quantos anos a pessoa
# vai se aposentar.

from datetime import date
from time import sleep
ano = date.today().year
from operator import itemgetter

print('-='*20)
print('{:^40}'.format('PROGRAMA DE CADASTRO DE PESSOAS'))
print('-='*20)

cadastro = {'Nome': str(input('Digite o nome:  ')).capitalize()}
nascimento = int(input('Digite o ano de nascimento:  '))
cadastro['Idade'] = ano - nascimento
cadastro['CTPS'] = int(input('Digite o n° da Carteira de Trabalho:  '))

if cadastro['CTPS'] != 0:
    cadastro['1° Contratação'] = int(input('Digite o ano de contratação:  '))
    cadastro['Salário'] = float(input('{}'.format('Digite o salário:  ')))
    contagem = cadastro['1° Contratação'] + 35
    cadastro['Aposentadoria'] = contagem - nascimento

print('-='*20)
print('{:^40}'.format('Mostrando Resultados'))
print('-='*20)

for k, v in cadastro.items():
        print(f'{k} >> {v}.')
