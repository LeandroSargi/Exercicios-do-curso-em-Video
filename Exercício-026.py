frase = str(input('Por favor, digite uma frase qualquer:\n')).lower() .strip()
print('A letra A aparece {} vez(es) na frase!!'.format(frase.count('a')))
print('A primeira vez na posição {}.'.format(frase.find('a')+1))
print('A última vez na posição {}.'.format(frase.rfind('a')+1))
