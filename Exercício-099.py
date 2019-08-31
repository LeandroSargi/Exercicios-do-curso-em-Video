# Faça um programa que tenha uma função chada maior(), que receba vários
# parâmetros com valores inteiros.
# Seu programa tem que analizar todos os valores e dizer qual deles é
# o maior.
from time import sleep

def maior(* núm):
    print('-='*30)
    print('Analisando os valores passados...')
    maior = 0
    for c, v in enumerate(núm):
        if c == 0:
            maior = v
        else:
            if maior < v:
                maior = v
        print(f'{v} ', end= '', flush=True)
        sleep(.3)
    print(f' | Foram informados {len(núm)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.', end= '')
    print()

maior(1, 88, 3, 25, 9, 77, 36, 14)
maior(95, 3, 9, 15, 33, 99, 10)
maior(6)
maior()
