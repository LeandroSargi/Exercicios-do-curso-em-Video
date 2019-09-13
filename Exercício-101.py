#Crie um programa que tenha uma função chamada voto() que vai receber
#como parâmetro o ano de nascimento de uma pessoa, retornando um valor
#literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO
#nas eleiçoes.

def voto (ano):
    """

    """
    from datetime import date
    atual = date.today().year
    idade = atual - nasc
    if idade < 16:
        return f'Com idade {idade}: NÃO VOTA!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com idade {idade}: VOTO OPCIONAL!'
    else:
        return f'Com idade {idade}: VOTO OBRIGATÓRIO!!'


#Programa principal
nasc = int(input('Digite o ano de seu nascimento:  '))
print(voto(nasc))
