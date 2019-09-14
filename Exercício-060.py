#Faça um programa que leia um número inteiro qualquer e mostre na tela o seu fatorial:

#minha solução

num = int(input('Digite um número para calcular o Fatorial:')) #variável recebendo numero

contador = num #contador recebendo mesmo valor do número para usar no laço de repetição
#não posso usar o número, porque este deve permanecer o mesmo para fazer o cálculo

fatorial = 1 #esta variável irá multiplicar o contador por 1 inicialmente
#após pegar o resultado, irá armazenar e multiplicar pelos outros contadores assim por diante
#com isso teremos o resultado final

print('Calculando {}! = '.format(num), end = '') #exibe o valor do número digitado
while contador > 0: #quando o contador chegar a 1 o laço de repetição para
    print('{}'.format(contador), end = '') #mostrando contador a cada repetição diminui um da contagem
    print(' x ' if contador > 1 else ' = ', end = '') # imprime um sinal de x do lado do contador até que seja maior que 1
#assim que o contador chegar a 1, o sinal exibe =
    fatorial *= contador #multiplica os valores e os armazena na variável para exibir o resultado no final
    contador -= 1 #recebe menos 1 a cada repetição
print('{}'.format(fatorial)) #mostra o resultado





