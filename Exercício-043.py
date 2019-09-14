print('Bem vindo a calculadora de Índice de massa corporal!!')
peso = float(input('Por favor, digite quantos quilos você pesa:\n'))
altura = float(input('Agora digite a sua altura em metros:\n'))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu IMC é {:.2f}, você está abaixo do peso ideal.'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é {:.2f}, você está no peso Ideal!!'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é {:.2f}, você está com Sobrepeso!'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é {:.2f}, você está com Obesidade!'.format(imc))
else:
    print('Seu IMC é {:.2f}, você está com obesidade mórbida, cuidado!!'.format(imc))