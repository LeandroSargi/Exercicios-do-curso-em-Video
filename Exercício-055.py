#Programa que lê o peso de 5 pessoas e diz qual foi o maior e o menor peso

maior = 0 #contagem de peso maior iniciada no 0
menor = 0 #contagem de peso menor iniciada no 0

for pess in range (1, 6): #contagem de pessoas do 1 ao 5
    peso = float(input('Digite o peso da {}° pessoa:\n'.format(pess))) #peso recebendo dados, contagem de pessoas no laço pess
    if pess == 1: '''se pess(pessoa) for igual a 1, ou seja, primeiro laço,
    tanto a variável maior como a menor, recebem o primeiro peso.'''
        maior = peso
        menor = peso
    else: #caso contrário, a partir do segundo laço, começam as hipóteses
        if peso > maior: #se peso for mais que "maior", então "maior" recebe peso.
            maior = peso
        elif peso < menor: #se peso for menor que "menor", então "menor" recebe peso.
            menor = peso
print('O maior peso lido foi de {}Kg!'.format(maior)) #exibindo resultados
print('O menor peso lido foi de {}Kg!'.format(menor))