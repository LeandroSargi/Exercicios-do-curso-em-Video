# Faça um mini sistema que utilize o Interactive Help do Python, o usuário
# vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a
# palavra 'FIM' o programa se encerrará.
#OBS: use cores

from time import sleep

c = ('\033[m',          # 0 - sem cor
     '\033[30;41m',     # 1 - vermelho
     '\033[30;42m',     # 2 - verde
     '\033[30;43m',     # 3 - amarelo
     '\033[30;44m',     # 4 - azul
     '\033[30;45m',     # 5 - roxo
     '\033[7;30m'       # 6 - branco
     )


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('-'*tam)
    print(f'  {msg}')
    print('-'*tam)
    print(c[0], end='')
    sleep(1)


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\':', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


#Programa Principal


while True:
    titulo('Sistema de ajuda PyHelP', 2)
    comando = str(input('Função ou Biblioteca [Digite FIM para encerrar]: '))
    if comando.upper() == 'FIM':
        titulo('FINALIZANDO...', 1)
        break
    else:
        ajuda(comando.lower())
