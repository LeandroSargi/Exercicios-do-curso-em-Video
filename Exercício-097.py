# Faça um programa que tenha uma função chamada escreva(), que receba
# um texto qualquer como parâmetro e mostre uma mensagem com tamanho
# adaptável.
# Ex: escreva('Olá mundo')
# -----------------
#    olá mundo
# -----------------


def escreva(texto):
    print('#'*30)
    print('{:^30}'.format(texto))
    print('#'*30)

texto = str(input('Digite algo aqui:  '))
escreva(texto)
