soma = 0
for c in range (0, 6):
    numero = int(input('Digite um numero inteiro:\n'))
    if numero % 2 == 0:
        soma += numero
print(soma)