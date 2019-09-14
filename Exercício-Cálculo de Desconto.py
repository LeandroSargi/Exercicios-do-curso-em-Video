print('Este programa tem a função de ler um valor em reais, e mostrar seu novo valor com desconto!')
r = float(input('Digite um valor em reais:\n'))
d = float(input('Entre com o valor do desconto em porcentagem:\n'))
print('Você digitou o valor de R${:.2f} reais, com {:.2f}% de desconto seu novo valor é de R${:.2f} reais!!'.format(r, d, r-(r*(d/100))))