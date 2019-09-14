frase = str(input('Digite uma frase:\n')).strip() .lower() .split()
frase = ''.join(frase)
inverso = '' #inverso recebe vazio para entrar no laço for
for letra in range(len(frase) -1, -1, -1):


''' letra no laço mostra a frase da posição -1 que no caso é a última letra da frase.
Pois se a primeira letra fica na posição zero, a última fica na -1.

O segundo -1 depois da vírgula significa a mesma coisa, porém como o python termina sua
contagem com um antes do fim, ele vai parar na posição zero.

E o último -1 é a contagem de casas que se dá na forma negativa, ou descrecente, ou inversa.

 '''
    inverso += frase[letra] #o inverso que estava nulo, recebe a frase concatenada
print('Você digitou {}, o inverso é {}.'.format(frase, inverso))
if frase == inverso:
    print('É palíndromo!!')
else:
    print('Não é palíndromo!')






#if frase == frase2[::-1]:
