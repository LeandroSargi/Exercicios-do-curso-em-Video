#Crie um programa que tenha uma função fatorial() que receba dois
#parâmetros: o primeiro que indique o número a calcular e o outro
#chamado show, que será um valor lógico (opcional) indicando se será
#mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show=False):
    """
    --> Calcula o fatorial de um número.
    :param num: recebe o valor para cálculo do fatorial.
    :param show: mostra ou não as etapas do cálculo (padrão=False).
    :return: retorna o resultado do fatorial do parâmetro num.
    """
    fat = 1
    c = num
    while c > 0:
        if show:
            print(f'{c} ', end='')
            if c > 1:
                print(f'{"x"} ', end='')
            else:
                print(f'{"="} ', end='')
        fat *= c
        c -= 1
    return(fat)


#Programa Principal
num = int(input('Digite um número para saber o seu fatorial:'))
print(fatorial(num, show=True))
#help(fatorial)
