print('\033[1;35mBem vindo ao seu assistente de cálculo para viagens!!')
dist = int(input('Digite a distância da sua viagem em quilômetros:\033[m\n'))
if dist <= 200:
    print('\033[1;33mA sua viagem custará R${:.2f} Reais!!'.format(dist*0.5))
else:
    print('\033[1;31mA sua viagem custará R${:.2f} Reais!!'.format(dist*0.45))
