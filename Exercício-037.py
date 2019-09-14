print('Bem vindo ao conversor de bases numéricas!')
inteiro = int(input('Por favor, entre com um número inteiro decimal para a conversão:\n'))
print("""Agora selecione para qual base numérica deseja converter:
        1 - Para binário;
        2 - Para base octal;
        3 - Para base hexadecimal.""")
alternativa = int(input('Digite a opção desejada:\n'))
if alternativa == 1:
    print('{} em binário é: {}'.format(inteiro, bin(inteiro)[2:]))
elif alternativa == 2:
    print('{} em octal é: {}'.format(inteiro, oct(inteiro)[2:]))
elif alternativa == 3:
    print('{} em Hexadecimal é: {}'.format(inteiro, hex(inteiro)[2:]))
else:
    print('Opção inválida, tente novamente.')