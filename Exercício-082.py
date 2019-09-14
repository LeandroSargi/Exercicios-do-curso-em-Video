'''Crie um programa que vai ler vários números e colocá-los numa lista.
Depois disso crie duas listas extras que vão conter apenas os valores
pares e os valores impares digitados.
Ao final, mostre o conteúdo das três listas geradas.'''

numeros = list()
pares = list()
impares = list()

while True:
    valor = int(input('\033[1;32mDigite um valor:   '))
    numeros.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

    opção = str(input('Quer continuar? [S/ N]:  ')) .strip() .upper() [0]
    if opção in 'N':
        break
print(f'Você digitou os seguintes valores: {numeros}.')
if pares == list():
    print('Não foram digitados números pares!')
else:
    print(f'Os números pares são os seguintes:  {pares}.')
if impares == list():
    print('Não foram digitados números impares!')
else:
    print(f'E os ímpares são:   {impares}.')
