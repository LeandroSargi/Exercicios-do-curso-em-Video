'''Crie um programa que tenha uma tupla com várias palavras (sem acentos).
Depois disso você deve mostrar para cada palavra, quais são suas vogais.'''

palavras = ('aprender', 'sucesso', 'python', 'realização', 'atualização', 'desenvolvimento', 'criar', 'inovar')
#tupla recebe palavras

for item in palavras: #o laço vai percorrer cada palavra da tupla
    print(f'\033[1;33m\nNa palavra {item.upper()} temos: ', end='') #aqui todas as palavras serão impressas
    #uma por linha, acompanhadas da frase em questão
    for letra in item: #para cada letra de cada palavra
        if letra.lower() in 'aeiou': #se a palavra conter uma dessas letras, irá imprimir a letra em questão
            print(letra, end= ' ')