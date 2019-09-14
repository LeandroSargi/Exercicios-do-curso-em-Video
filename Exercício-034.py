print('Olá, bem vindo ao programa de cálculo de aumento de salário')
sal = float(input('Por favor, digite o valor do seu salário:\n'))
if sal <= 1250:
    sal = sal + (sal*(15/100))
    print('O seu novo salário é R${:.2f} reais.'.format(sal))
else:
    sal = sal + (sal*(10/100))
    print('O seu novo salário é R${:.2f} reais.'.format(sal))