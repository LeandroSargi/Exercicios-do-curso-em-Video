#Crie um programa que leia vários números pelo teclado e no final.
#Apresente qual a média entre eles, e também o maior e o menor valor digitado.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


soma = contador  = maior  = menor = 0 #variáveis recebendo o valor zero
numero = int(input('Por favor digite um número [0 PARA SAIR]:\n')) #entrada de dados com número inteiro
while numero != 0: #o laço se repete enquanto a variável número for diferente de zero
    soma += numero #soma recebe soma (que é zero) mais o número digitado no início
    contador += 1 #contador conta quantos laços se repetiram, ou seja, quantos números foram digitados
    if contador == 1: #para o primeiro numero digitado, o menor e o maior recebem o mesmo numero
        maior = menor = numero #variável maior e menor recebendo o valor de número
    else: #se não for o primeiro número, segue a sequencia abaixo
        if numero > maior: #se numero for maior que a variável maior, ela o recebe
            maior = numero #variável recebendo número em caso afirmativo
        if numero < menor: #se o numero for menor que a variável menor, ela o recebe
            menor = numero #variável recebendo número
    numero = int(input('Por favor digite um número [0 PARA SAIR]:\n')) #aqui é dado a entrada de número novamente
#se ela for igual a zero, não é contabilizado nada e o laço para de se repetir


print('Você digitou {} números. A média entre eles foi {}.'.format(contador, soma/contador))
#aqui é exibido o contador, que conta quantas repetições aconteceram, mais a soma e a média
print('O maior número digitado foi {}, e o menor foi {}.'.format(maior, menor))
#exibe o maior e o menor numero digitados
