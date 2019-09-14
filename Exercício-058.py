from random import randint
numeropc = randint(0,10)
palpite = 0
acertou = False
print('Computador diz: Eu pensei em um número que está entre 0 e 10!!')
print('Tente adivinhar em qual número estou pensando...\n')
while not acertou:
    meunumero = int(input('Qual o seu palpite?\n'))
    palpite += 1
    if meunumero == numeropc:
        acertou = True
    else:
        if meunumero < numeropc:
            print('É Mais... Tente outra vez:\n')
        elif meunumero > numeropc:
            print('É Menos.... Tente outra vez:\n')


print('Parabéns, vc acertou!! O número que pensei foi {}!!'.format(numeropc))
if palpite == 1:
    print('Você conseguiu adivinhar o resultado usando {} palpite.'.format(palpite))
else:
    print('Você conseguiu adivinhar o resultado usando {} palpites.'.format(palpite))