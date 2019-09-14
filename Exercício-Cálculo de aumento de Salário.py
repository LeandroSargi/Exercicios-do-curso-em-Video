print('Olá, você acaba de receber um aumento!!\n'
      'Vamos descobrir seu novo salário?')
s = float(input('Digite o valor do seu último salário:\n'))
a = float(input('Agora digite qual foi a sua porcentagem de aumento:\n'))
print('Ok!! Você digitou a quantia de R${:.2f} reais, com {:.2f}% de aumento, '
      'seu salário passa a ser de R${:.2f} reais!!'.format(s, a, s+(s*(a/100))))