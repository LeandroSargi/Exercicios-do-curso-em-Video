# Crie um programa que tenha a função leiaint(), que vai funcionar de forma
# semelhante a função input() do Python, só que fazendo a validação para
# aceitar apenas um valor numérico.
# Ex: n= leiaint('Digite um número:  ')

def leiaint(msg): #definição de função
    ok = False #condição recebe falso
    valor = 0 #variavel auxiliar recebe zero
    while True:
        n = str(input(msg)) #mostra a mensagem do programa Principal
        # e armazena na variável n o resultado obtido
        if n.isnumeric(): #se o n for numérico
            valor = int(n) #a variavel valor recebe n convertido em inteiro
            ok = True #parâmetro ok recebe verdadeiro
        else:
            print('ERRO! VOCÊ NÃO DIGITOU UM VALOR NUMÉRICO.')
        #caso contrário é impressa uma tela de erro fazendo o
        #usuário digitar novamente um valor válido
        if ok:
            break #se estiver tudo ok o laço é interrompido
    return valor #retorna a variável valor

#Programa Principal
n = leiaint('Digite um número qualquer:  ') #texto que será levado para
# dentro do while na função leiaint
print(f'Você digitou o número {n}') #a variável valor é impressa em n
