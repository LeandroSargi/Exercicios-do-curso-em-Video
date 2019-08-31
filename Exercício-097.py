# Faça um programa que tenha uma função chamada escreva(), que receba
# um texto qualquer como parâmetro e mostre uma mensagem com tamanho
# adaptável.
# Ex: escreva('Olá mundo')
# -----------------
#    olá mundo
# -----------------


def escreva(texto):
    tam = len(texto) + 4
    print('#'*tam)
    print(f'  {texto}')
    print('#'*tam)


#Programa Principal
escreva('Leandro Antunes Sargi')
escreva('Olá Mundo!!')
escreva('oi')
