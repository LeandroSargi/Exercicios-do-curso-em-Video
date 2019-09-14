#programa que lê o ano de nascimento de sete pessoas e diz quem já é de maior
from datetime import date #módulo de datas

totmaior = 0 #contador para pessoas maiores de idade
totmenor = 0 #contador para pessoas menores de idade
for pess in range (1, 8): #pess(pessoa) começa a contar do 1 e vai até o 7
    nasc = int(input('Digite o ano de nascimento da {}° pessoa:'.format(pess))) #usando o laço para exibir a contagem das pessoas
    idade = date.today().year - nasc #a fórmula pega o ano atual e já subtrai pelo nascimento, resultando a idade
    if idade >= 18:
        totmaior += 1 #contador recebendo uma pessoa, se ela for maior
    else:
        totmenor += 1 #contador recebendo uma pessoa se ela for menor

print('Ao todo tivemos {} pessoa(s) maior(es) de idade'.format(totmaior))
print('E também tivemos {} pessoa(s) menor(es) de idade'.format(totmenor))
