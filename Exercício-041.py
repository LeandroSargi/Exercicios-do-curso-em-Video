from datetime import date
print('Você está no programa da confederação nacional de natação!')
nasc = int(input('Por favor, digite o ano de nascimento do Atleta para mostrar a sua categoria:\n'))
idade = date.today().year - nasc
if idade <= 9:
    print('Você tem {} anos e pertence a categoria Mirim!'.format(idade))
elif idade > 9 and idade <= 14:
    print('Você tem {} anos e pertence a categoria Infantil!'.format(idade))
elif idade > 14 and idade <=19:
    print('Você tem {} anos e pertence a categoria JÚnior!'.format(idade))
elif idade > 19 and idade <=20:
    print('Você tem {} anos e pertence a categoria Sênior!'.format(idade))
else:
    print('Você tem mais de 20 anos e pertence a categoria Master!'.format(idade))
