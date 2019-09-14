print('Bora fazer tabuada? kkkkkkkkk\n'
      'Este programa pega um número digitado e mostra na tela a sua tabuada!!')
n = int(input('Digite o número do qual deseja saber a tabuada:\n'))
for c in range (0,11):
    print('{}x{} = {}'.format(n, c, n*c))

