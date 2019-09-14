pt = int(input('Digite o primeiro termo da PA:'))
r = int(input('Digite a razão da PA:'))
decimo = pt + (10-1) * r #fórmula para encontrar o décimo termo da pa
for c in range (pt, decimo + r, r):
    print(c)