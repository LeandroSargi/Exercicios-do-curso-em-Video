from random import randint
numeropc = randint(0,5)
print('Computador diz: Eu pensei em um número que está entre 0 e 5!!')
meunumero = int(input('Tente adivinhar em qual número estou pensando:\n'))
if meunumero == numeropc:
    print('Parabéns, vc acertou!! O número que pensei foi {}!!'.format(numeropc))
else:
    print('Que pena, você não acertou, tente novamente!')