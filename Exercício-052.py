numero = int(input('Digite um número:'))
tot = 0
for c in range(1, numero + 1): #contador começa no 1 e termina com um a mais que a variável, para contar até o valor da variável
    if numero % c== 0: #se a divisão do número pelo contador for igual a zero
        print('\033[33m', end='') #imprime o número na cor amarela
        tot += 1 #conta o número de vezes que o número foi divisivel com resto zero
    else:
        print('\033[31m', end='') #imprime o número na cor vermelha
    print('{} '.format(c), end='') #imprime todos os números
print('\n\033[mO número {} foi divisível {} vezes!!'.format(numero, tot)) #limpa a formatação e diz quantas vezes foi dividido
if tot == 2:
    print('E por isso ele é Primo!!')
else:
    print('E por isso ele não é Primo!!')
