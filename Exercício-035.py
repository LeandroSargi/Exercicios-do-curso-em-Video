print(20*'-=''-')
print('Analizador de triângulos')
print(20*'-=''-')

r1 = float(input('Digite o valor do comprimento da primeira reta do triângulo:\n'))
r2 = float(input('Agora digite o valor do comprimento da segunda reta:\n'))
r3 = float(input('Estamos quase lá, agora digite o valor da terceira reta:\n'))

if r1 < r2+r3 and r2 < r1 + r3 and r3 < r1+r2:
    print('As retas podem formar um triângulo!!')
else:
    print('As retas não podem formar um triângulo!')