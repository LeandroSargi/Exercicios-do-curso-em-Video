#digitar 5 numeros e colocá-los em ordem na lista sem usar o sort

lista = list()

for c in range(0, 5):
    num = int(input(f'Digite o {c+1}° numero inteiro:  '))
    if len(lista) == 0 or num > lista[-1]:
        lista.append(num)
        print(lista)
    else:
        for pos, n in enumerate(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break


print(lista)