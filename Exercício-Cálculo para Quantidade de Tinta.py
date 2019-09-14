print('Bem vindo ao programa que te ajuda a calcular a quantidade de tinta necessária para pintar uma parede!!')
l = float(input('Por favor, digite a largura da parede em metros, separando casas decimais por pontos:\n'))
a = float(input('Agora digite a altura da parede, levando em conta o mesmo quesito anterior:\n'))
t = 2
print('Ok! Você possui uma parede com {:.2f} m² (metros quadrados).\n'
      'Para pintar esta parede por completo você vai precisar de {:.2f} litros de tinta!'.format(l*a, (l*a)/2))