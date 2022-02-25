print('Montador de Progressões Aritméticas v. 2')

t1 = int(input('Digite o primeiro número de uma P.A: '))
r = int(input('Digite um número para ser a razão de uma P.A: '))
pa = list()

termo = t1
c = 1

while c <= 10:
    pa.append(termo)
    termo += r
    c += 1

print(pa)
