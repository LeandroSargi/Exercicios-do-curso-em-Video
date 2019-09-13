def teste(x, y, z):
	a= str(input(x))
	b= str(input(y))
	c= str(input(z))
	return a, b, c

g= teste('Digite um numero:  ')
h= teste('Digite uma frase:  ')
i= teste('Digite um texto:  ')

teste(x=g, y=h, z=i)
print(f'{a} {b} {c}')
