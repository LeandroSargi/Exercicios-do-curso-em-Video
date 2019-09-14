from datetime import date

print('Bem vindo ao programa de alistamento do exército!')
ano = int(input('Por favor, digite o ano do seu nascimento:\n'))
idade = date.today().year - ano


if idade < 18:
    print('Você ainda não está da idade para se alistar, faltam {} ano(s)!'.format(18-idade))
elif idade == 18:
    print('Você está na idade correta para o alistamento!! Faça-o ainda este ano!')
elif idade > 18:
    print('Seu tempo de se alistar já passou, você está {} ano(s) em atraso.'.format(idade - 18))
