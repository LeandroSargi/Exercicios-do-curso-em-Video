#Ex 104 - Crie um programa que tenha a função leiaint(), que vai funcionar de
#forma semelhante a função input() do Python, só que fazendo a validação para
#aceitar somente valores numéricos.

def leiaint(msg):
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            break
        else:
            print('\033[1;31mERRO!! Digite um número inteiro válido.\033[m')
    return valor

#Programa Principal
n = leiaint('Digite um numero inteiro:  ')
print(f'O número digitado foi {n}.')