#Crie um programa que tenha uma função fatorial() que receba dois
#parâmetros: o primeiro que indique o número a calcular e o outro
#chamado show, que será um valor lógico (opcional) indicando se será
#mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num):
    fat = 1
    c = num
    while c > 0:
        fat *= c
        c -= 1
    return(fat)

# def show():
#     if show True:



num = int(input('Digite um número para saber o seu fatorial:'))

print(fatorial(num))
