nome = str(input('Digite o nome da sua Cidade:'))
nome = nome.title()
nome = nome.split()
if 'Santo' in nome[0]:
    print('Sua cidade começa com o nome santo!')
else:
    print('Sua cidade não começa com o nome Santo.')