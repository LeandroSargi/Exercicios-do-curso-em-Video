#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa mostrar:
#A média de idade do grupo, nome do homem mais velho, quantas mulheres tem menos de 20 anos.

somaidade = 0
mediaidade = 0
homemmaisvelho = 0
nomevelho = ''
totmulher20 = 0

for pess in range (1, 5):
    print('------ {}° PESSOA ------'.format(pess))
    nome = str(input('Nome: ')) .strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')) .strip()
    somaidade += idade
    if pess == 1 and sexo in 'mM':
        homemmaisvelho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > homemmaisvelho:
        homemmaisvelho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4

print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(homemmaisvelho, nomevelho))
print('Ao todo, são {} mulher(es) com menos de 20 anos.'.format(totmulher20))