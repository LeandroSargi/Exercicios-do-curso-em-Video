import math
print('Bem vindo ao programa que calcula o seno, cosseno e tangente de um ângulo!!')
an = float(input('Por favor, digite o ângulo:\n'))
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tg = math.tan(math.radians(an))
print('O ângulo de {}, tem o seno de {:.2f}, o cosseno de {:.2f} e a tangente de {:.2f}'.format(an, seno, cosseno, tg))
1xcz