print('Olá, vamos descobrir quantos dólares você pode comprar?')
d = float(input('Digite o valor em reais que você possui:\n'))
print('Ok!! Você possui a quantia de R${:.2f} reais, você pode comprar US$ {:.2f} dólares!!'.format(d, d/3.27))