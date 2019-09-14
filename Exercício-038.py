print('Bem vindo ao comparador de números!!')
x = int(input('Digite o primeiro número a ser comparado:\n'))
y = int(input('Digite o segundo número:\n'))
if x>y:
    print('O primeiro número é maior!')
elif x<y:
    print('O segundo número é maior!')
elif x==y:
    print('Não existe diferença, os dois números são iguais!')
