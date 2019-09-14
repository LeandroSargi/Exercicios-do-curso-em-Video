cores = {'Amarelo':'\033[1;33m', 'Vermelho':'\033[1;31m', 'Roxo':'\033[1;35m', 'Normal':'\033[m'}
print(cores['Roxo'],'Bem vindo ao programa detector de PAR ou ÍMPAR!!')
numero = int(input('Digite um número por favor:\n'))
resultado = numero % 2
if resultado == 0:
    print('{} O número {} é{} PAR{}!!'.format(cores['Normal'], numero, cores['Amarelo'], cores['Normal']))
else:
    print('{} O número {} é{} ÍMPAR{}!!'.format(cores['Normal'], numero, cores['Vermelho'], cores['Normal']))