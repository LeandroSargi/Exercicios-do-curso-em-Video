import random
print('Bem vindo ao jogo JOKENPÔ!!')
print('A máquina irá escolher uma opção e depois é a sua vez!')
rodada = 0
maq = 0
eu = 0
while rodada < 5:
    joken = ['Pedra', 'Papel', 'Tesoura']
    pc = random.choice(joken)
    print("""Pronto! A máquina já escolheu, agora é a sua vez:
            Pedra;
            Papel;
            Tesoura.""")
    user = str(input('Digite sua escolha:\n')).strip() .title()
    if user == 'Pedra' or user == 'Papel' or user == 'Tesoura':
        if user == 'Pedra' and pc == 'Pedra' or user == 'Papel' and pc == 'Papel' or user == 'Tesoura' and pc == 'Tesoura':
            print('Você e a máquina escolheram a mesma opção, tente novamente!!')
        elif user == 'Pedra' and pc == 'Papel':
            print('Papel amassa Pedra, a máquina venceu!!')
            maq = maq + 1
        elif user == 'Papel' and pc == 'Tesoura':
            print('Tesoura corta Papel, a máquina venceu!!')
            maq = maq + 1
        elif user == 'Tesoura' and pc == 'Pedra':
            print('Pedra quebra Tesoura, a máquina venceu!!')
            maq = maq + 1
        elif pc == 'Pedra' and user == 'Papel':
            print('Papel amassa Pedra, você venceu!!')
            eu = eu + 1
        elif pc == 'Papel' and user == 'Tesoura':
            print('Tesoura corta Papel, você venceu!!')
            eu = eu + 1
        elif pc == 'Tesoura' and user == 'Pedra':
            print('Pedra quebra Tesoura, você venceu!!')
            eu = eu + 1
    else:
        print('Opcão inválida, tente novamente!!')
    rodada = rodada + 1
if maq <= eu:
    print('O jogo terminou!! Placar: VOCê {} x {} MÁQUINA'.format(eu, maq))
elif eu < maq:
    print('O jogo terminou!! Placar: MÁQUINA {} x {} VOCÊ'.format(maq, eu))
