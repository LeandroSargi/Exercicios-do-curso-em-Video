#Faça um programa que mostre os dez primeiros termos de uma progressão aritmética.
#Usando a estrutura de repetição while
#Melhore perguntado ao usuário, se ele deseja mostrar mais termos.


print('Gerador de PA')
print('-='*10)
pt = int(input('Digite o Primeiro Termo da PA:\n'))
r = int(input('Digite a Razão da PA:\n'))
termo = pt
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} --> '.format(termo), end = '')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?\n '))
print('-----------Progressão finalizada com {} termos exibidos!-----------'.format(total))
