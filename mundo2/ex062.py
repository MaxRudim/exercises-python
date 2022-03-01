print('Montador de Progressões Aritméticas v. 2 Aprimorado')

t1 = int(input('Digite o primeiro número de uma P.A: '))
r = int(input('Digite um número para ser a razão de uma P.A: '))
pa = list()

termo = t1
c = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while c <= total:
        pa.append(termo)
        termo += r
        c += 1

    print(pa)
    mais = int(input('\nQuantos termos voce quer mostrar a mais? [0] = FIM: '))

print(f'Fim, voce mostrou um total de {len(pa)} termos')
