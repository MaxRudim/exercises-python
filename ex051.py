
print('Montador de Progressões Aritméticas')

t1 = int(input('Digite o primeiro número de uma P.A: '))
r = int(input('Digite um número para ser a razão de uma P.A: '))
tenth = t1 + (10 - 1) * r
pa = list()

for num in range(t1, tenth + r, r):
    pa.append(num)

print(pa)
