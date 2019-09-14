#Crie um programa que leia dois valores e mostre um menu na tela:
#[1]somar // [2] multiplicar // [3] maior // [4] novos números // [5] sair do programa
from time import sleep

num1 = int(input('Digite o primeiro número:\n'))
num2 = int(input('Digite o segundo número:\n'))
opção = 0


while opção != 5:
    opção = int(input('>>>>>>>Digite a opção desejada<<<<<<<<<\n\n'
                      '     [1] - Para Somar os números;\n\n'
                      '     [2] - Para multiplicar os números;\n\n'
                      '     [3] - Para ver entre os números qual é o maior;\n\n'
                      '     [4] - Para escolher novos números;\n\n'
                      '     [5] - Sair do programa.\n'))
    if opção == 1:
        soma = num1 + num2
        print('A soma entre {} + {} é {}.'.format(num1, num2, soma))
    elif opção == 2:
        mult = num1 * num2
        print('O resultado de {} x {} é {}.'.format(num1, num2, mult))
    elif opção == 3:
        if num1 > num2:
            maior = num1
            print('O maior entre {} e {} é {}.'.format(num1, num2, maior))
        elif num2 == num1:
            print('Os dois números digitados são iguais, não existe maior!!')
        else:
            maior = num2
            print('O maior entre {} e {} é {}.'.format(num1, num2, maior))
    elif opção == 4:
        print('Por favor escolha os números novamente!')
        num1 = int(input('Digite o primeiro número:\n'))
        num2 = int(input('Digite o segundo número:\n'))
    elif opção == 5:
        print('Finalizando.....')
    else:
        print('Opção inválida, tente novamente!')
    print('=-='*15)
    sleep(1.5)
print('Fim do programa!! Volte Sempre!!')

