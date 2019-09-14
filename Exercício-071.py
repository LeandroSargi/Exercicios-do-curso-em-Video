print('\033[1;35m='*30) #imprimindo o título (linhas)
print('{:^30}'.format('BANCO CEV')) #título
print('='*30) #linhas novamente
valor = int(input('Que valor voçê quer sacar? R$\n')) #variavel recebendo valor
total = valor #variavel total recebendo valor
cedula = 50 #valor da primeira nota a ser considerada
totalcedula = 0 #total de notas recebe zero
while True: #repetição infinita
    if total >= cedula: #se o total for maior que o valor da nota em questão
        total -= cedula #total é subtraído pelo valor da nota
        totalcedula += 1 #a nota recebe um para a contagem a cada repetição
    else: #caso contrário
        if totalcedula > 0: #se o total de cédulas for maior que zero
            print(f'Total de {totalcedula} cédulas de R${cedula}') #imprima o numero de cédulas da cédula em questão
        if cedula == 50: #se a cédula for igual a 50, faça a célular receber 20
            cedula = 20 #célula recebe o valor e sai deste if, retornando para o while True
        elif cedula == 20: #senão, se a célula for igual a 20, faça-a receber 10
            cedula = 10 #célula recebe o valor de 10
        elif cedula == 10 #senão, se a célula for igual a 10, faça-a receber 1
            cedula = 1 #célula recebe o valor de 1
        totalcedula = 0 #SEMPRE QUE A CÉDULA RECEBER UM NOVO VALOR, O TOTAL DE CÉLULAS RECEBE ZERO.
        if total == 0: #quando o valor total do dinheiro for igual a zero....
            break #pare as repetições

print('='*30) #imprima as linhas
print('Volte sempre ao BANCO CEV! Tenha um bom dia!!') #texto final