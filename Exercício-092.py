# Crie um programa que leia nome, ano de nascimento e carteira de trabalho
# e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for
# diferente de zero, o dicionário receberá também o ano de contratação e o
# salário. Calcule e acrescente, além da idade, com quantos anos a pessoa
# vai se aposentar.

from datetime import date
ano = date.today().year
from operator import itemgetter


cadastro = {'Nome': str(input('Digite o nome:  ')),
'Idade': ano - int(input('Digite o ano de nascimento:  ')),
'Carteira': int(input('Digite o número de sua Carteira de Trabalho:  '))}

if cadastro['Carteira'] != 0:
    cadastro['Contrato'] = int(input('Digite o ano de contratação:  '))
    cadastro['Salário'] = float(input('{:.2f}'.format('Digite o salário:  ')))

# para se aposentar é 35 anos de contribuição
print(cadastro)
