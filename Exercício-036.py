print('Bem vindo ao programa de cálculo de empréstimo para casa própria!')
casa = float(input('Por favor, digite o valor do imóvel que você deseja comprar:\n'))
renda = float(input('Agora digite o valor da sua renda mensal:\n'))
parcelas = int(input('Agora digite em quantos anos deseja pagar o imóvel:\n'))
meses = parcelas*12
valor = casa / meses
if valor <= renda*(30/100):
    print('Você foi aprovado para comprar o imóvel!!\n'
          'Sua parcela será de R${:.2f} reais, seu pagamento será feito em {} ano(s).'.format(valor, parcelas))
else:
    print('Infelizmente não foi possível conceder o crédito para você, sua parcela ultrapassou 30% de sua renda.')