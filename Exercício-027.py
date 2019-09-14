nome = str(input('Por favor, digite seu nome completo:\n')).strip() .title()
print('Olá {}, prazer em te conhecer!!'.format(nome))
nome = nome.split()
print('O seu primeiro nome é {} e o seu último nome é {}!!'.format(nome[0], nome[-1]))