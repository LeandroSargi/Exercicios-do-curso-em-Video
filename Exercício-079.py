'''Crie um programa onde o usuário possa cadastrar vários valores numéricos.
Caso o número já exista na lista, ele não será adicionado.
No final serão exibidos todos os valores únicos digitados, em ordem crescente.'''

opção = ''
lista  = list()


while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
        print(f'Valor {} adicionado com sucesso!')
    else:
        print('Este valor já está na lista, valor não cadastrado!')
    opção = str(input('Você deseja continuar? [S / N]:  ')).strip().upper()[0]
    if opção in 'Nn':
        break


print(f'Você digitou os valores {sorted(lista)}.')