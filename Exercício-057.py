#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
#Caso esteja errado, peça digitação novamente até ter o resultado certo.

sexo = str(input('Digite seu sexo:\n'
            '[M] Para Masculino;\n'
            '[F] Para Feminino.\n')).strip().upper()[0]

while sexo not in 'MF':
    sexo = str(input('Dados inválidos, digite seu sexo novamente:\n')).strip().upper()[0]
print('Sexo {} registrado com sucesso!!'.format(sexo))
