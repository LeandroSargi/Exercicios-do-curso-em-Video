#sequencia de fibonacci

print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30) #impressão do título

n = int(input('Digite quantos números da sequência você deseja exibir:\n')) #variável recebe o número de termos
#que serão exibidos
t1 = 0 #primeiro termo da sequênia de fibonacci é sempre 0
t2 = 1 #o segundo termo da sequência é sempre 1
print('{} --> {} '.format(t1, t2), end= '') #aqui é a impressão na tela do primeiro e segundo termo, sem pular linhas.
cont = 3 #o contador está recebendo 3 porque a sequência já está com o primeiro e segundo termos definidos

while cont <= n: #enquanto o contador for menor ou igual o numero de termos, o laço se repete
    t3 = t1 + t2 #o terceiro termo recebe a soma do primeiro com o segundo, como manda a sequência
    print('--> {} --> '.format (t3), end= '') #impressão na tela do terceiro termo, junto ao primeiro e segundo
#devido a configuração que está fora do laço para não pular linhas
    cont +=1 #aqui o contador recebe mais um número a cada repetição, e vai parar o laço quando chegar ao
#valor de n.
    t1 = t2 #aqui o primeiro termo recebe o valor do segundo termo a cada repetição sucessivamente
    t2 = t3 #aqui o segundo termo recebe o valor do terceiro termo a cada repetição sucessivamente
print('FIM')
