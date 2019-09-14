print('Bem vindo ao programa de cálculo de notas para alunos!!')
n1 = float(input('Por favor, digite a primeira nota a ser calculada:\n'))
n2 = float(input('Agora digite a segunda nota:\n'))
nf = (n1+n2)/2

if nf < 5.0:
    print('Sua nota foi {:.2f}, infelizmente você foi reprovado por ter ficado abaixo da média.'.format(nf))
elif nf > 5.0 and nf < 6.9:
    print('Sua média foi {:.2f}, você está de recuperação.'.format(nf))
elif nf >= 6.9:
    print('Parabéns!! Sua média foi {:.2f}, você foi aprovado!!'.format(nf))
