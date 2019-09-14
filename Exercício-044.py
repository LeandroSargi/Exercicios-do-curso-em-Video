print('Bem vindo ao simulador de vendas!!')
valor = float(input('Digite o valor do produto em reais:\n'))
pagamento = int(input("""Agora digite a opção para a forma de pagamento desejada:
    1 - Pagamento á vista em dinheiro e cheque (10% de desconto).
    2 - Á vista no cartão (5% de desconto).
    3 - Em até 2x no cartão (preço normal).
    4 - 3x ou mais no cartão (20% de juros).
Digite a opção desejada:\n"""))
if pagamento == 1:
    print('O valor do seu produto com desconto será de R${:.2f} Reais.'.format(valor - (valor*10/100)))
elif pagamento == 2:
    print('O valor do seu produto com desconto será de R${:.2f} Reais.'.format(valor - (valor*5/100)))
elif pagamento == 3:
    print('O valor de seu produto será R${:.2f} Reais.'.format(valor))
    valor = valor / 2
    print('Parcelado ficará 2x de R${:.2f} Reais!'.format(valor))
elif pagamento == 4:
    valor = valor + (valor*20/100)
    parcela = int(input('Deseja parcelar em quantas vezes?\n'))
    print('O valor do seu produto com acréscimo fica em R${:.2f} Reais.'.format(valor))
    valor = valor / parcela
    print('Ficará {} parcelas de R${:.2f} Reais!'.format(parcela, valor))
else:
    print('Opção inválida, tente novamente!')

