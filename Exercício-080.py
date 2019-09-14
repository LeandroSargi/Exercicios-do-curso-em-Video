'''Crie um programa onde o usuário possa digitar 5 valores numéricos
e cadastre-os em uma lista já na posição correta sem usar o sort().
No final, mostre a lista ordenada na tela.'''

numeros = list() #LISTA VAZIA PARA COMEÇAR

for n in range(1,6): #LAÇO FOR DE 1 ATÉ 6 (5 REPETIÇÕES)
    valor = int(input(f'Digite o {n}° número:\n')) #ENTRADA DE VALORES
    if n == 1 or valor > numeros[-1]: #SE FOR O PRIMEIRO LAÇO OU SE O VALOR FOR MAIOR QUE O ÚLTIMO ITEM DA LISTA
        numeros.append(valor) #NUMEROS RECEBE VALOR
        print(f'Valor {valor} cadastrado com sucesso!')
    else: #SENÃO
        pos = 0 #VARIAVEL POS RECEBE ZERO
        while pos < len(numeros): #ENQUANTO A VARIAVEL POS FOR MENOR QUE O TAMANHO DA LISTA
            if valor <= numeros[pos]: #SE O VALOR FOR MENOR OU IGUAL AO ITEM DA LISTA NA POSIÇÃO MENCIONADA
                numeros.insert(pos, valor) #LISTA RECEBE NA POSIÇÃO MENCIONADA O VALOR
                print(f'Número {valor} adicionado na posição {pos}.')
                break #PARA O LAÇO ASSIM QUE A VARIAVEL POS CHEGAR AO TAMANHO DA LISTA
            pos += 1

print('-='*30)
print(f'Os números digitados foram {numeros}.')