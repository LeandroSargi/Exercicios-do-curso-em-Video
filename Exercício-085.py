'''Crie um programa onde o usuário possa cadastrar sete valores numéricos
e possa cadastrá-los em uma lista única que mantenha separado
os valores pares dos ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.'''

lista = ([], [])
dados = list()

for c in range (1, 8):
    dados.append(int(input(f'Digite o {c}º número inteiro:  ')))
for n in dados:
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()

print(f'Os números pares digitados foram {lista[0]}.')
print(f'Os números ímpares digitados foram {lista[1]}.')
