
numero = 0
cont = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        cont += 1
        numero += c
print('A soma de todos os {} dígitos foi {}!'.format(cont, numero))
