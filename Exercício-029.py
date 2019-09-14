print('Olá, este é o sistema dos Guardas de Trânsito!')
print('A velocidade máxima permitida aqui é 80km/h!\n'
      'Caso alguém ultrapassar o limite eu direi o valor da multa!')
limite = 80
vel = int(input('Por favor, digite a velocidade do veículo em Km/h:\n'))
if vel <= limite:
    print('Você está respeitando as leis!! Boa viagem!!')
else:
    print('Sua velocidade é de {} Km/h, {} Km/h acima do limite.\n'
          'Sua multa será de R$ {:.2f} Reais, respeite as leis!'.format(vel, vel-limite, (vel-limite)*7))