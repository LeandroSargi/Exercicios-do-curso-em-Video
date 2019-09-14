#Crie um programa que leia vários números inteiros pelo teclado
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual a soma entre eles.
#Desconsiderando o flag. (999)
numero = contador = soma = 0 #aqui temos 3 variáveis recebendo o mesmo valor que é zero
numero = int(input('Por favor digite um número inteiro [999 para finalizar]:\n'))
#variável onde será armazendada a entrada de números
while numero != 999: #enquanto numero for diferente de 999 o laço se repete
    soma += numero #soma recebe soma que atualmente é zero e grava o número digitado no início do programa
    contador += 1 #contador que atualmente é zero, recebe o contador mais 1
#o contador serve apenas para exibir quantos numeros eu digitei (neste caso)
    numero = int(input('Por favor digite um número inteiro [999 para finalizar]:\n')) #entrada de dados para mais um número, caso ele
#seja igual a 999, o laço para na hora e não é gravado mais nenhuma informação.
print('Você digitou {} números.'.format(contador)) #toda vez que é digitado um número no começo do programa
#o contador recebe um, oque faz com que ele mostre a quantidade de números digitados.
#Ele não conta o 999, porque assim que o 999 for digitado, o laço para
print('A soma desses números é {}.'.format(soma)) #a soma recebe sempre o valor do número digitado e
#soma com o que estiver gravado nela, se está fora do laço considera o valor do início do programa
#e quando entra no laço, ela armazena tudo que é digitado dentro dele.
print('ACABOU!!')